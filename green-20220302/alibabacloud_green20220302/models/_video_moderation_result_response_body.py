# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class VideoModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.VideoModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The moderation results.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.VideoModerationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class VideoModerationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_result: main_models.VideoModerationResultResponseBodyDataAudioResult = None,
        data_id: str = None,
        frame_result: main_models.VideoModerationResultResponseBodyDataFrameResult = None,
        live_id: str = None,
        manual_task_id: str = None,
        risk_level: str = None,
        task_id: str = None,
    ):
        # The voice moderation results. The moderation results contain a structure.
        self.audio_result = audio_result
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, the dataId field is not available in the response.
        self.data_id = data_id
        # The image moderation results. If the call is successful, the HTTP status code 200 and moderation results are returned. The moderation results contain a structure.
        self.frame_result = frame_result
        # The unique ID of the live stream.
        self.live_id = live_id
        self.manual_task_id = manual_task_id
        # Risk Level.
        self.risk_level = risk_level
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.audio_result:
            self.audio_result.validate()
        if self.frame_result:
            self.frame_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_result is not None:
            result['AudioResult'] = self.audio_result.to_map()

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.frame_result is not None:
            result['FrameResult'] = self.frame_result.to_map()

        if self.live_id is not None:
            result['LiveId'] = self.live_id

        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioResult') is not None:
            temp_model = main_models.VideoModerationResultResponseBodyDataAudioResult()
            self.audio_result = temp_model.from_map(m.get('AudioResult'))

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('FrameResult') is not None:
            temp_model = main_models.VideoModerationResultResponseBodyDataFrameResult()
            self.frame_result = temp_model.from_map(m.get('FrameResult'))

        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')

        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class VideoModerationResultResponseBodyDataFrameResult(DaraModel):
    def __init__(
        self,
        frame_num: int = None,
        frame_summarys: List[main_models.VideoModerationResultResponseBodyDataFrameResultFrameSummarys] = None,
        frames: List[main_models.VideoModerationResultResponseBodyDataFrameResultFrames] = None,
        risk_level: str = None,
    ):
        # The number of captured frames that are returned for the video file.
        self.frame_num = frame_num
        # The summary of the labels against which captured frames are matched.
        self.frame_summarys = frame_summarys
        # The information about the frames that match the labels.
        self.frames = frames
        # Risk Level.
        self.risk_level = risk_level

    def validate(self):
        if self.frame_summarys:
            for v1 in self.frame_summarys:
                 if v1:
                    v1.validate()
        if self.frames:
            for v1 in self.frames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num

        result['FrameSummarys'] = []
        if self.frame_summarys is not None:
            for k1 in self.frame_summarys:
                result['FrameSummarys'].append(k1.to_map() if k1 else None)

        result['Frames'] = []
        if self.frames is not None:
            for k1 in self.frames:
                result['Frames'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')

        self.frame_summarys = []
        if m.get('FrameSummarys') is not None:
            for k1 in m.get('FrameSummarys'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFrameSummarys()
                self.frame_summarys.append(temp_model.from_map(k1))

        self.frames = []
        if m.get('Frames') is not None:
            for k1 in m.get('Frames'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFrames()
                self.frames.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class VideoModerationResultResponseBodyDataFrameResultFrames(DaraModel):
    def __init__(
        self,
        offset: float = None,
        results: List[main_models.VideoModerationResultResponseBodyDataFrameResultFramesResults] = None,
        risk_level: str = None,
        temp_url: str = None,
        timestamp: int = None,
    ):
        # The interval between the start of the video file and the captured frame. Unit: seconds.
        self.offset = offset
        # The results of frame moderation parameters such as the label parameter and the confidence parameter.
        self.results = results
        # Risk Level.
        self.risk_level = risk_level
        # The temporary URL of a captured frame.
        self.temp_url = temp_url
        # The absolute timestamp. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset is not None:
            result['Offset'] = self.offset

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.temp_url is not None:
            result['TempUrl'] = self.temp_url

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TempUrl') is not None:
            self.temp_url = m.get('TempUrl')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class VideoModerationResultResponseBodyDataFrameResultFramesResults(DaraModel):
    def __init__(
        self,
        custom_image: List[main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage] = None,
        logo_data: List[main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoData] = None,
        public_figure: List[main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure] = None,
        result: List[main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsResult] = None,
        service: str = None,
        text_in_image: Dict[str, Any] = None,
    ):
        # If a custom image library is hit, information about the custom image library is returned.
        self.custom_image = custom_image
        # Returns logo information when the video contains a logo.
        self.logo_data = logo_data
        # If the video contains a specific figure, the code of the identified figure is returned.
        self.public_figure = public_figure
        # The results of frame moderation parameters such as the label parameter and the confidence parameter.
        self.result = result
        # The moderation service that is called.
        self.service = service
        # The information about the text hit in the image is returned.
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for v1 in self.custom_image:
                 if v1:
                    v1.validate()
        if self.logo_data:
            for v1 in self.logo_data:
                 if v1:
                    v1.validate()
        if self.public_figure:
            for v1 in self.public_figure:
                 if v1:
                    v1.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k1 in self.custom_image:
                result['CustomImage'].append(k1.to_map() if k1 else None)

        result['LogoData'] = []
        if self.logo_data is not None:
            for k1 in self.logo_data:
                result['LogoData'].append(k1.to_map() if k1 else None)

        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k1 in self.public_figure:
                result['PublicFigure'].append(k1.to_map() if k1 else None)

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.service is not None:
            result['Service'] = self.service

        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k1 in m.get('CustomImage'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage()
                self.custom_image.append(temp_model.from_map(k1))

        self.logo_data = []
        if m.get('LogoData') is not None:
            for k1 in m.get('LogoData'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoData()
                self.logo_data.append(temp_model.from_map(k1))

        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k1 in m.get('PublicFigure'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure()
                self.public_figure.append(temp_model.from_map(k1))

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('TextInImage') is not None:
            self.text_in_image = m.get('TextInImage')

        return self

class VideoModerationResultResponseBodyDataFrameResultFramesResultsResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The description of the result.
        self.description = description
        # The label returned after a frame is moderated. Multiple risk labels and the corresponding scores of confidence levels may be returned for a frame.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure(DaraModel):
    def __init__(
        self,
        figure_id: str = None,
        figure_name: str = None,
        location: List[main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigureLocation] = None,
    ):
        # The information about the code of the identified figure.
        self.figure_id = figure_id
        self.figure_name = figure_name
        self.location = location

    def validate(self):
        if self.location:
            for v1 in self.location:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id

        if self.figure_name is not None:
            result['FigureName'] = self.figure_name

        result['Location'] = []
        if self.location is not None:
            for k1 in self.location:
                result['Location'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')

        if m.get('FigureName') is not None:
            self.figure_name = m.get('FigureName')

        self.location = []
        if m.get('Location') is not None:
            for k1 in m.get('Location'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigureLocation()
                self.location.append(temp_model.from_map(k1))

        return self

class VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigureLocation(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoData(DaraModel):
    def __init__(
        self,
        location: main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoDataLocation = None,
        logo: List[main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoDataLogo] = None,
    ):
        # The location of the logo.
        self.location = location
        # Logo information.
        self.logo = logo

    def validate(self):
        if self.location:
            self.location.validate()
        if self.logo:
            for v1 in self.logo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location is not None:
            result['Location'] = self.location.to_map()

        result['Logo'] = []
        if self.logo is not None:
            for k1 in self.logo:
                result['Logo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoDataLocation()
            self.location = temp_model.from_map(m.get('Location'))

        self.logo = []
        if m.get('Logo') is not None:
            for k1 in m.get('Logo'):
                temp_model = main_models.VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoDataLogo()
                self.logo.append(temp_model.from_map(k1))

        return self

class VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoDataLogo(DaraModel):
    def __init__(
        self,
        confidence: int = None,
        label: str = None,
        name: str = None,
    ):
        # Confidence score, ranging from 0 to 100, with two decimal places.
        self.confidence = confidence
        # label
        self.label = label
        # Logo name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['confidence'] = self.confidence

        if self.label is not None:
            result['label'] = self.label

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class VideoModerationResultResponseBodyDataFrameResultFramesResultsLogoDataLocation(DaraModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The height of the text area. Unit: pixels.
        self.h = h
        # The width of the text area. Unit: pixels.
        self.w = w
        # The distance from the top-left corner of the text area to the y-axis, with the top-left corner of the image as the origin. Unit: pixels.
        self.x = x
        # The distance from the top-left corner of the text area to the x-axis, with the top-left corner of the image as the origin. Unit: pixels.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        lib_id: str = None,
    ):
        # The ID of the custom image that is hit.
        self.image_id = image_id
        # The ID of the custom image library that is hit.
        self.lib_id = lib_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        return self

class VideoModerationResultResponseBodyDataFrameResultFrameSummarys(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        label_sum: int = None,
    ):
        # The description of the result.
        self.description = description
        # The label against which a captured frame is matched.
        self.label = label
        # The number of times that the label is matched.
        self.label_sum = label_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')

        return self

class VideoModerationResultResponseBodyDataAudioResult(DaraModel):
    def __init__(
        self,
        audio_summarys: List[main_models.VideoModerationResultResponseBodyDataAudioResultAudioSummarys] = None,
        risk_level: str = None,
        slice_details: List[main_models.VideoModerationResultResponseBodyDataAudioResultSliceDetails] = None,
    ):
        # Summary of voice labels.
        self.audio_summarys = audio_summarys
        # Risk Level.
        self.risk_level = risk_level
        # The details about the text in the moderated voice. The value is a JSON array that contains one or more elements. Each element corresponds to a text entry.
        self.slice_details = slice_details

    def validate(self):
        if self.audio_summarys:
            for v1 in self.audio_summarys:
                 if v1:
                    v1.validate()
        if self.slice_details:
            for v1 in self.slice_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioSummarys'] = []
        if self.audio_summarys is not None:
            for k1 in self.audio_summarys:
                result['AudioSummarys'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k1 in self.slice_details:
                result['SliceDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_summarys = []
        if m.get('AudioSummarys') is not None:
            for k1 in m.get('AudioSummarys'):
                temp_model = main_models.VideoModerationResultResponseBodyDataAudioResultAudioSummarys()
                self.audio_summarys.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k1 in m.get('SliceDetails'):
                temp_model = main_models.VideoModerationResultResponseBodyDataAudioResultSliceDetails()
                self.slice_details.append(temp_model.from_map(k1))

        return self

class VideoModerationResultResponseBodyDataAudioResultSliceDetails(DaraModel):
    def __init__(
        self,
        descriptions: str = None,
        end_time: int = None,
        end_timestamp: int = None,
        extend: str = None,
        labels: str = None,
        risk_level: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        # The description of the labels.
        self.descriptions = descriptions
        # The end time of the text after voice-to-text conversion. Unit: seconds.
        self.end_time = end_time
        # The end timestamp of the segment. Unit: milliseconds.
        self.end_timestamp = end_timestamp
        # A reserved parameter.
        self.extend = extend
        # The details of the labels.
        self.labels = labels
        # Risk Level.
        self.risk_level = risk_level
        # Subcategory labels. Multiple labels are separated by commas (,).
        self.risk_tips = risk_tips
        # The risk words that are hit. Multiple words are separated by commas (,).
        self.risk_words = risk_words
        # The risk score. Default range: 0 to 99.
        self.score = score
        # The start time of the text after voice-to-text conversion. Unit: seconds.
        self.start_time = start_time
        # The start timestamp of the segment. Unit: milliseconds.
        self.start_timestamp = start_timestamp
        # The text converted from voice.
        self.text = text
        # If the moderation object is a voice stream, this parameter indicates the temporary access URL of the voice stream to which the text entry corresponds. The validity period of the URL is 30 minutes. You must prepare another URL to store the voice stream at the earliest opportunity.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.descriptions is not None:
            result['Descriptions'] = self.descriptions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips

        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words

        if self.score is not None:
            result['Score'] = self.score

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.text is not None:
            result['Text'] = self.text

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Descriptions') is not None:
            self.descriptions = m.get('Descriptions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')

        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class VideoModerationResultResponseBodyDataAudioResultAudioSummarys(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        label_sum: int = None,
    ):
        # The description of the labels.
        self.description = description
        # The voice label.
        self.label = label
        # The number of times that the label is matched.
        self.label_sum = label_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')

        return self

