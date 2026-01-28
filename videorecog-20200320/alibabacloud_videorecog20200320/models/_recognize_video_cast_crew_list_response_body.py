# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_videorecog20200320 import models as main_models
from darabonba.model import DaraModel

class RecognizeVideoCastCrewListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.RecognizeVideoCastCrewListResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.RecognizeVideoCastCrewListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RecognizeVideoCastCrewListResponseBodyData(DaraModel):
    def __init__(
        self,
        cast_results: List[main_models.RecognizeVideoCastCrewListResponseBodyDataCastResults] = None,
        ocr_results: List[main_models.RecognizeVideoCastCrewListResponseBodyDataOcrResults] = None,
        ocr_results_url: str = None,
        ocr_video_results_url: str = None,
        subtitles_results: List[main_models.RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults] = None,
        video_ocr_results: List[main_models.RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults] = None,
    ):
        self.cast_results = cast_results
        self.ocr_results = ocr_results
        self.ocr_results_url = ocr_results_url
        self.ocr_video_results_url = ocr_video_results_url
        self.subtitles_results = subtitles_results
        self.video_ocr_results = video_ocr_results

    def validate(self):
        if self.cast_results:
            for v1 in self.cast_results:
                 if v1:
                    v1.validate()
        if self.ocr_results:
            for v1 in self.ocr_results:
                 if v1:
                    v1.validate()
        if self.subtitles_results:
            for v1 in self.subtitles_results:
                 if v1:
                    v1.validate()
        if self.video_ocr_results:
            for v1 in self.video_ocr_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CastResults'] = []
        if self.cast_results is not None:
            for k1 in self.cast_results:
                result['CastResults'].append(k1.to_map() if k1 else None)

        result['OcrResults'] = []
        if self.ocr_results is not None:
            for k1 in self.ocr_results:
                result['OcrResults'].append(k1.to_map() if k1 else None)

        if self.ocr_results_url is not None:
            result['OcrResultsUrl'] = self.ocr_results_url

        if self.ocr_video_results_url is not None:
            result['OcrVideoResultsUrl'] = self.ocr_video_results_url

        result['SubtitlesResults'] = []
        if self.subtitles_results is not None:
            for k1 in self.subtitles_results:
                result['SubtitlesResults'].append(k1.to_map() if k1 else None)

        result['VideoOcrResults'] = []
        if self.video_ocr_results is not None:
            for k1 in self.video_ocr_results:
                result['VideoOcrResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cast_results = []
        if m.get('CastResults') is not None:
            for k1 in m.get('CastResults'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataCastResults()
                self.cast_results.append(temp_model.from_map(k1))

        self.ocr_results = []
        if m.get('OcrResults') is not None:
            for k1 in m.get('OcrResults'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataOcrResults()
                self.ocr_results.append(temp_model.from_map(k1))

        if m.get('OcrResultsUrl') is not None:
            self.ocr_results_url = m.get('OcrResultsUrl')

        if m.get('OcrVideoResultsUrl') is not None:
            self.ocr_video_results_url = m.get('OcrVideoResultsUrl')

        self.subtitles_results = []
        if m.get('SubtitlesResults') is not None:
            for k1 in m.get('SubtitlesResults'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults()
                self.subtitles_results.append(temp_model.from_map(k1))

        self.video_ocr_results = []
        if m.get('VideoOcrResults') is not None:
            for k1 in m.get('VideoOcrResults'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults()
                self.video_ocr_results.append(temp_model.from_map(k1))

        return self

class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResults(DaraModel):
    def __init__(
        self,
        detail_info: List[main_models.RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfo] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_info = detail_info
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        if self.detail_info:
            for v1 in self.detail_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k1 in self.detail_info:
                result['DetailInfo'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k1 in m.get('DetailInfo'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfo()
                self.detail_info.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfo(DaraModel):
    def __init__(
        self,
        boxes: List[int] = None,
        position: List[main_models.RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoPosition] = None,
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
            for v1 in self.position:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boxes is not None:
            result['Boxes'] = self.boxes

        result['Position'] = []
        if self.position is not None:
            for k1 in self.position:
                result['Position'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Position'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoPosition()
                self.position.append(temp_model.from_map(k1))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('TextType') is not None:
            self.text_type = m.get('TextType')

        return self

class RecognizeVideoCastCrewListResponseBodyDataVideoOcrResultsDetailInfoPosition(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class RecognizeVideoCastCrewListResponseBodyDataSubtitlesResults(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class RecognizeVideoCastCrewListResponseBodyDataOcrResults(DaraModel):
    def __init__(
        self,
        detail_info: List[main_models.RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfo] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_info = detail_info
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        if self.detail_info:
            for v1 in self.detail_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k1 in self.detail_info:
                result['DetailInfo'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k1 in m.get('DetailInfo'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfo()
                self.detail_info.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfo(DaraModel):
    def __init__(
        self,
        boxes: List[int] = None,
        char_probs: List[List[float]] = None,
        frame_index: int = None,
        position: List[main_models.RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoPosition] = None,
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
            for v1 in self.position:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boxes is not None:
            result['Boxes'] = self.boxes

        if self.char_probs is not None:
            result['CharProbs'] = self.char_probs

        if self.frame_index is not None:
            result['FrameIndex'] = self.frame_index

        result['Position'] = []
        if self.position is not None:
            for k1 in self.position:
                result['Position'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Position'):
                temp_model = main_models.RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoPosition()
                self.position.append(temp_model.from_map(k1))

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

class RecognizeVideoCastCrewListResponseBodyDataOcrResultsDetailInfoPosition(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class RecognizeVideoCastCrewListResponseBodyDataCastResults(DaraModel):
    def __init__(
        self,
        detail_info: Dict[str, str] = None,
        end_time: float = None,
        start_time: float = None,
    ):
        self.detail_info = detail_info
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            self.detail_info = m.get('DetailInfo')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

