# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, BinaryIO, Dict


class ScanImageRequestTask(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        image_time_millisecond: int = None,
        image_url: str = None,
        interval: int = None,
        max_frames: int = None,
    ):
        self.data_id = data_id
        self.image_time_millisecond = image_time_millisecond
        # This parameter is required.
        self.image_url = image_url
        self.interval = interval
        self.max_frames = max_frames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.image_time_millisecond is not None:
            result['ImageTimeMillisecond'] = self.image_time_millisecond
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ImageTimeMillisecond') is not None:
            self.image_time_millisecond = m.get('ImageTimeMillisecond')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        return self


class ScanImageRequest(TeaModel):
    def __init__(
        self,
        scene: List[str] = None,
        task: List[ScanImageRequestTask] = None,
    ):
        # 1
        # 
        # This parameter is required.
        self.scene = scene
        # 1
        # 
        # This parameter is required.
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['Scene'] = self.scene
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = ScanImageRequestTask()
                self.task.append(temp_model.from_map(k))
        return self


class ScanImageAdvanceRequestTask(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        image_time_millisecond: int = None,
        image_urlobject: BinaryIO = None,
        interval: int = None,
        max_frames: int = None,
    ):
        self.data_id = data_id
        self.image_time_millisecond = image_time_millisecond
        # This parameter is required.
        self.image_urlobject = image_urlobject
        self.interval = interval
        self.max_frames = max_frames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.image_time_millisecond is not None:
            result['ImageTimeMillisecond'] = self.image_time_millisecond
        if self.image_urlobject is not None:
            result['ImageURL'] = self.image_urlobject
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.max_frames is not None:
            result['MaxFrames'] = self.max_frames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ImageTimeMillisecond') is not None:
            self.image_time_millisecond = m.get('ImageTimeMillisecond')
        if m.get('ImageURL') is not None:
            self.image_urlobject = m.get('ImageURL')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('MaxFrames') is not None:
            self.max_frames = m.get('MaxFrames')
        return self


class ScanImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        scene: List[str] = None,
        task: List[ScanImageAdvanceRequestTask] = None,
    ):
        # 1
        # 
        # This parameter is required.
        self.scene = scene
        # 1
        # 
        # This parameter is required.
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['Scene'] = self.scene
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = ScanImageAdvanceRequestTask()
                self.task.append(temp_model.from_map(k))
        return self


class ScanImageResponseBodyDataResultsSubResultsFrames(TeaModel):
    def __init__(
        self,
        rate: float = None,
        url: str = None,
    ):
        self.rate = rate
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class ScanImageResponseBodyDataResultsSubResultsHintWordsInfoList(TeaModel):
    def __init__(
        self,
        context: str = None,
    ):
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        return self


class ScanImageResponseBodyDataResultsSubResultsLogoDataList(TeaModel):
    def __init__(
        self,
        height: float = None,
        name: str = None,
        type: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.height = height
        self.name = name
        self.type = type
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class ScanImageResponseBodyDataResultsSubResultsProgramCodeDataList(TeaModel):
    def __init__(
        self,
        height: float = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

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
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class ScanImageResponseBodyDataResultsSubResultsSfaceDataListFaces(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        rate: float = None,
    ):
        self.id = id
        self.name = name
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.rate is not None:
            result['Rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        return self


class ScanImageResponseBodyDataResultsSubResultsSfaceDataList(TeaModel):
    def __init__(
        self,
        faces: List[ScanImageResponseBodyDataResultsSubResultsSfaceDataListFaces] = None,
        height: float = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.faces = faces
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = ScanImageResponseBodyDataResultsSubResultsSfaceDataListFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class ScanImageResponseBodyDataResultsSubResults(TeaModel):
    def __init__(
        self,
        frames: List[ScanImageResponseBodyDataResultsSubResultsFrames] = None,
        hint_words_info_list: List[ScanImageResponseBodyDataResultsSubResultsHintWordsInfoList] = None,
        label: str = None,
        logo_data_list: List[ScanImageResponseBodyDataResultsSubResultsLogoDataList] = None,
        ocrdata_list: List[str] = None,
        program_code_data_list: List[ScanImageResponseBodyDataResultsSubResultsProgramCodeDataList] = None,
        rate: float = None,
        scene: str = None,
        sface_data_list: List[ScanImageResponseBodyDataResultsSubResultsSfaceDataList] = None,
        suggestion: str = None,
    ):
        self.frames = frames
        self.hint_words_info_list = hint_words_info_list
        self.label = label
        self.logo_data_list = logo_data_list
        # 1
        self.ocrdata_list = ocrdata_list
        self.program_code_data_list = program_code_data_list
        self.rate = rate
        self.scene = scene
        self.sface_data_list = sface_data_list
        self.suggestion = suggestion

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()
        if self.hint_words_info_list:
            for k in self.hint_words_info_list:
                if k:
                    k.validate()
        if self.logo_data_list:
            for k in self.logo_data_list:
                if k:
                    k.validate()
        if self.program_code_data_list:
            for k in self.program_code_data_list:
                if k:
                    k.validate()
        if self.sface_data_list:
            for k in self.sface_data_list:
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
        result['HintWordsInfoList'] = []
        if self.hint_words_info_list is not None:
            for k in self.hint_words_info_list:
                result['HintWordsInfoList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        result['LogoDataList'] = []
        if self.logo_data_list is not None:
            for k in self.logo_data_list:
                result['LogoDataList'].append(k.to_map() if k else None)
        if self.ocrdata_list is not None:
            result['OCRDataList'] = self.ocrdata_list
        result['ProgramCodeDataList'] = []
        if self.program_code_data_list is not None:
            for k in self.program_code_data_list:
                result['ProgramCodeDataList'].append(k.to_map() if k else None)
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.scene is not None:
            result['Scene'] = self.scene
        result['SfaceDataList'] = []
        if self.sface_data_list is not None:
            for k in self.sface_data_list:
                result['SfaceDataList'].append(k.to_map() if k else None)
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = ScanImageResponseBodyDataResultsSubResultsFrames()
                self.frames.append(temp_model.from_map(k))
        self.hint_words_info_list = []
        if m.get('HintWordsInfoList') is not None:
            for k in m.get('HintWordsInfoList'):
                temp_model = ScanImageResponseBodyDataResultsSubResultsHintWordsInfoList()
                self.hint_words_info_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.logo_data_list = []
        if m.get('LogoDataList') is not None:
            for k in m.get('LogoDataList'):
                temp_model = ScanImageResponseBodyDataResultsSubResultsLogoDataList()
                self.logo_data_list.append(temp_model.from_map(k))
        if m.get('OCRDataList') is not None:
            self.ocrdata_list = m.get('OCRDataList')
        self.program_code_data_list = []
        if m.get('ProgramCodeDataList') is not None:
            for k in m.get('ProgramCodeDataList'):
                temp_model = ScanImageResponseBodyDataResultsSubResultsProgramCodeDataList()
                self.program_code_data_list.append(temp_model.from_map(k))
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        self.sface_data_list = []
        if m.get('SfaceDataList') is not None:
            for k in m.get('SfaceDataList'):
                temp_model = ScanImageResponseBodyDataResultsSubResultsSfaceDataList()
                self.sface_data_list.append(temp_model.from_map(k))
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class ScanImageResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        image_url: str = None,
        sub_results: List[ScanImageResponseBodyDataResultsSubResults] = None,
        task_id: str = None,
    ):
        self.data_id = data_id
        self.image_url = image_url
        self.sub_results = sub_results
        self.task_id = task_id

    def validate(self):
        if self.sub_results:
            for k in self.sub_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        result['SubResults'] = []
        if self.sub_results is not None:
            for k in self.sub_results:
                result['SubResults'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        self.sub_results = []
        if m.get('SubResults') is not None:
            for k in m.get('SubResults'):
                temp_model = ScanImageResponseBodyDataResultsSubResults()
                self.sub_results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ScanImageResponseBodyData(TeaModel):
    def __init__(
        self,
        results: List[ScanImageResponseBodyDataResults] = None,
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
                temp_model = ScanImageResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        return self


class ScanImageResponseBody(TeaModel):
    def __init__(
        self,
        data: ScanImageResponseBodyData = None,
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
            temp_model = ScanImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScanImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScanImageResponseBody = None,
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
            temp_model = ScanImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScanTextRequestLabels(TeaModel):
    def __init__(
        self,
        label: str = None,
    ):
        # This parameter is required.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ScanTextRequestTasks(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # This parameter is required.
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


class ScanTextRequest(TeaModel):
    def __init__(
        self,
        labels: List[ScanTextRequestLabels] = None,
        tasks: List[ScanTextRequestTasks] = None,
    ):
        # 1
        # 
        # This parameter is required.
        self.labels = labels
        # 1
        # 
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ScanTextRequestLabels()
                self.labels.append(temp_model.from_map(k))
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ScanTextRequestTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ScanTextResponseBodyDataElementsResultsDetailsContexts(TeaModel):
    def __init__(
        self,
        context: str = None,
    ):
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        return self


class ScanTextResponseBodyDataElementsResultsDetails(TeaModel):
    def __init__(
        self,
        contexts: List[ScanTextResponseBodyDataElementsResultsDetailsContexts] = None,
        label: str = None,
    ):
        self.contexts = contexts
        self.label = label

    def validate(self):
        if self.contexts:
            for k in self.contexts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contexts'] = []
        if self.contexts is not None:
            for k in self.contexts:
                result['Contexts'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contexts = []
        if m.get('Contexts') is not None:
            for k in m.get('Contexts'):
                temp_model = ScanTextResponseBodyDataElementsResultsDetailsContexts()
                self.contexts.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ScanTextResponseBodyDataElementsResults(TeaModel):
    def __init__(
        self,
        details: List[ScanTextResponseBodyDataElementsResultsDetails] = None,
        label: str = None,
        rate: float = None,
        suggestion: str = None,
    ):
        self.details = details
        self.label = label
        self.rate = rate
        self.suggestion = suggestion

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = ScanTextResponseBodyDataElementsResultsDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class ScanTextResponseBodyDataElements(TeaModel):
    def __init__(
        self,
        results: List[ScanTextResponseBodyDataElementsResults] = None,
        task_id: str = None,
    ):
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
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ScanTextResponseBodyDataElementsResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ScanTextResponseBodyData(TeaModel):
    def __init__(
        self,
        elements: List[ScanTextResponseBodyDataElements] = None,
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
                temp_model = ScanTextResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k))
        return self


class ScanTextResponseBody(TeaModel):
    def __init__(
        self,
        data: ScanTextResponseBodyData = None,
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
            temp_model = ScanTextResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ScanTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScanTextResponseBody = None,
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
            temp_model = ScanTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


