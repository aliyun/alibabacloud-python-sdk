# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMediaAuditResultResponseBody(DaraModel):
    def __init__(
        self,
        media_audit_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResult = None,
        request_id: str = None,
    ):
        # The review results.
        self.media_audit_result = media_audit_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media_audit_result:
            self.media_audit_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_audit_result is not None:
            result['MediaAuditResult'] = self.media_audit_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaAuditResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResult()
            self.media_audit_result = temp_model.from_map(m.get('MediaAuditResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResult(DaraModel):
    def __init__(
        self,
        abnormal_modules: str = None,
        audio_result: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultAudioResult] = None,
        image_result: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultImageResult] = None,
        label: str = None,
        suggestion: str = None,
        text_result: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultTextResult] = None,
        video_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResult = None,
    ):
        # The content that violates the regulations. Separate multiple values with commas (,). Valid values:
        # 
        # *   **video**
        # *   **image-cover**
        # *   **text-title**
        self.abnormal_modules = abnormal_modules
        # The results of audio review.
        self.audio_result = audio_result
        # The results of image review.
        self.image_result = image_result
        # The category of the review result. Separate multiple values with commas (,). Valid values:
        # 
        # *   **porn**
        # *   **terrorism**
        # *   **normal**
        self.label = label
        # The recommendation for review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
        self.suggestion = suggestion
        # The results of text review.
        self.text_result = text_result
        # The results of video review.
        self.video_result = video_result

    def validate(self):
        if self.audio_result:
            for v1 in self.audio_result:
                 if v1:
                    v1.validate()
        if self.image_result:
            for v1 in self.image_result:
                 if v1:
                    v1.validate()
        if self.text_result:
            for v1 in self.text_result:
                 if v1:
                    v1.validate()
        if self.video_result:
            self.video_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_modules is not None:
            result['AbnormalModules'] = self.abnormal_modules

        result['AudioResult'] = []
        if self.audio_result is not None:
            for k1 in self.audio_result:
                result['AudioResult'].append(k1.to_map() if k1 else None)

        result['ImageResult'] = []
        if self.image_result is not None:
            for k1 in self.image_result:
                result['ImageResult'].append(k1.to_map() if k1 else None)

        if self.label is not None:
            result['Label'] = self.label

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        result['TextResult'] = []
        if self.text_result is not None:
            for k1 in self.text_result:
                result['TextResult'].append(k1.to_map() if k1 else None)

        if self.video_result is not None:
            result['VideoResult'] = self.video_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalModules') is not None:
            self.abnormal_modules = m.get('AbnormalModules')

        self.audio_result = []
        if m.get('AudioResult') is not None:
            for k1 in m.get('AudioResult'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultAudioResult()
                self.audio_result.append(temp_model.from_map(k1))

        self.image_result = []
        if m.get('ImageResult') is not None:
            for k1 in m.get('ImageResult'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultImageResult()
                self.image_result.append(temp_model.from_map(k1))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.text_result = []
        if m.get('TextResult') is not None:
            for k1 in m.get('TextResult'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultTextResult()
                self.text_result.append(temp_model.from_map(k1))

        if m.get('VideoResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResult()
            self.video_result = temp_model.from_map(m.get('VideoResult'))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResult(DaraModel):
    def __init__(
        self,
        ad_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult = None,
        label: str = None,
        live_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult = None,
        logo_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult = None,
        porn_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult = None,
        suggestion: str = None,
        terrorism_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult = None,
    ):
        # The results of ad review.
        self.ad_result = ad_result
        # The category of the review result. Separate multiple values with commas (,). Valid values: 
        # 
        # - **porn**
        # - **terrorism**
        # - **normal**
        self.label = label
        # The results of undesired content review.
        self.live_result = live_result
        # The results of logo review.
        self.logo_result = logo_result
        # The results of pornographic content review.
        self.porn_result = porn_result
        # The recommendation for review results. Valid values:
        # 
        # - **block**
        # - **review**
        # - **pass**
        self.suggestion = suggestion
        # The results of terrorist content review.
        self.terrorism_result = terrorism_result

    def validate(self):
        if self.ad_result:
            self.ad_result.validate()
        if self.live_result:
            self.live_result.validate()
        if self.logo_result:
            self.logo_result.validate()
        if self.porn_result:
            self.porn_result.validate()
        if self.terrorism_result:
            self.terrorism_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_result is not None:
            result['AdResult'] = self.ad_result.to_map()

        if self.label is not None:
            result['Label'] = self.label

        if self.live_result is not None:
            result['LiveResult'] = self.live_result.to_map()

        if self.logo_result is not None:
            result['LogoResult'] = self.logo_result.to_map()

        if self.porn_result is not None:
            result['PornResult'] = self.porn_result.to_map()

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.terrorism_result is not None:
            result['TerrorismResult'] = self.terrorism_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult()
            self.ad_result = temp_model.from_map(m.get('AdResult'))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LiveResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult()
            self.live_result = temp_model.from_map(m.get('LiveResult'))

        if m.get('LogoResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult()
            self.logo_result = temp_model.from_map(m.get('LogoResult'))

        if m.get('PornResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult()
            self.porn_result = temp_model.from_map(m.get('PornResult'))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('TerrorismResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult()
            self.terrorism_result = temp_model.from_map(m.get('TerrorismResult'))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList] = None,
    ):
        # The average score of the review results.
        self.average_score = average_score
        # The statistics about tag frames.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # - **normal**
        # - **bloody**
        # - **explosion**
        # - **outfit**
        # - **logo**
        # - **weapon**
        # - **politics**
        # - **violence**
        # - **crowd**
        # - **parade**
        # - **carcrash**
        # - **flag**
        # - **location**
        # - **others**
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # - **block**
        # - **review**
        # - **pass**
        self.suggestion = suggestion
        # The information about the image with the highest score of the category that is indicated by Label.
        self.top_list = top_list

    def validate(self):
        if self.counter_list:
            for v1 in self.counter_list:
                 if v1:
                    v1.validate()
        if self.top_list:
            for v1 in self.top_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_score is not None:
            result['AverageScore'] = self.average_score

        result['CounterList'] = []
        if self.counter_list is not None:
            for k1 in self.counter_list:
                result['CounterList'].append(k1.to_map() if k1 else None)

        if self.label is not None:
            result['Label'] = self.label

        if self.max_score is not None:
            result['MaxScore'] = self.max_score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        result['TopList'] = []
        if self.top_list is not None:
            for k1 in self.top_list:
                result['TopList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')

        self.counter_list = []
        if m.get('CounterList') is not None:
            for k1 in m.get('CounterList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList()
                self.counter_list.append(temp_model.from_map(k1))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.top_list = []
        if m.get('TopList') is not None:
            for k1 in m.get('TopList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The category of the review result. Valid values:
        # 
        # - **normal**
        # - **bloody**
        # - **explosion**
        # - **outfit**
        # - **logo**
        # - **weapon**
        # - **politics**
        # - **violence**
        # - **crowd**
        # - **parade**
        # - **carcrash**
        # - **flag**
        # - **location**
        # - **others**
        self.label = label
        # The score of the image of the category that is indicated by Label.
        self.score = score
        # The position in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the image.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of frames.
        self.count = count
        # The category of the review result. Valid values:
        # 
        # - **normal**
        # - **bloody**
        # - **explosion**
        # - **outfit**
        # - **logo**
        # - **weapon**
        # - **politics**
        # - **violence**
        # - **crowd**
        # - **parade**
        # - **carcrash**
        # - **flag**
        # - **location**
        # - **others**
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList] = None,
    ):
        # The average score of the review results.
        self.average_score = average_score
        # The statistics about tag frames.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # - **porn**
        # - **sexy**
        # - **normal**
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The recommendation for review results.
        self.suggestion = suggestion
        # The information about the image with the highest score of the category that is indicated by Label.
        self.top_list = top_list

    def validate(self):
        if self.counter_list:
            for v1 in self.counter_list:
                 if v1:
                    v1.validate()
        if self.top_list:
            for v1 in self.top_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_score is not None:
            result['AverageScore'] = self.average_score

        result['CounterList'] = []
        if self.counter_list is not None:
            for k1 in self.counter_list:
                result['CounterList'].append(k1.to_map() if k1 else None)

        if self.label is not None:
            result['Label'] = self.label

        if self.max_score is not None:
            result['MaxScore'] = self.max_score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        result['TopList'] = []
        if self.top_list is not None:
            for k1 in self.top_list:
                result['TopList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')

        self.counter_list = []
        if m.get('CounterList') is not None:
            for k1 in m.get('CounterList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList()
                self.counter_list.append(temp_model.from_map(k1))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.top_list = []
        if m.get('TopList') is not None:
            for k1 in m.get('TopList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The category of the review result. Valid values:
        # 
        # - **porn**
        # - **sexy**
        # - **normal**
        self.label = label
        # The score of the image of the category that is indicated by Label.
        self.score = score
        # The position in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the image.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of frames.
        self.count = count
        # The category of the review result. Valid values:
        # 
        # - **porn**
        # - **sexy**
        # - **normal**
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList] = None,
    ):
        # The average score of the review results.
        self.average_score = average_score
        # The statistics about tag frames.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # - **logo**
        # - **normal**
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # - **block**
        # - **review**
        # - **pass**
        self.suggestion = suggestion
        # The information about the image with the highest score of the category that is indicated by Label.
        self.top_list = top_list

    def validate(self):
        if self.counter_list:
            for v1 in self.counter_list:
                 if v1:
                    v1.validate()
        if self.top_list:
            for v1 in self.top_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_score is not None:
            result['AverageScore'] = self.average_score

        result['CounterList'] = []
        if self.counter_list is not None:
            for k1 in self.counter_list:
                result['CounterList'].append(k1.to_map() if k1 else None)

        if self.label is not None:
            result['Label'] = self.label

        if self.max_score is not None:
            result['MaxScore'] = self.max_score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        result['TopList'] = []
        if self.top_list is not None:
            for k1 in self.top_list:
                result['TopList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')

        self.counter_list = []
        if m.get('CounterList') is not None:
            for k1 in m.get('CounterList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList()
                self.counter_list.append(temp_model.from_map(k1))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.top_list = []
        if m.get('TopList') is not None:
            for k1 in m.get('TopList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The category of the review result.
        # 
        # - **logo**
        # - **normal**
        self.label = label
        # The score of the image of the category that is indicated by Label.
        self.score = score
        # The position in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the image.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of frames.
        self.count = count
        # The category of the review result. Valid values:
        # 
        # - **logo**
        # - **normal**
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList] = None,
    ):
        # The average score of the review results.
        self.average_score = average_score
        # The statistics about tag frames.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # - **live**: The content contains undesirable scenes.
        # - **normal**: normal content.
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # - **block**
        # - **review**
        # - **pass**
        self.suggestion = suggestion
        # The information about the image with the highest score of the category that is indicated by Label.
        self.top_list = top_list

    def validate(self):
        if self.counter_list:
            for v1 in self.counter_list:
                 if v1:
                    v1.validate()
        if self.top_list:
            for v1 in self.top_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_score is not None:
            result['AverageScore'] = self.average_score

        result['CounterList'] = []
        if self.counter_list is not None:
            for k1 in self.counter_list:
                result['CounterList'].append(k1.to_map() if k1 else None)

        if self.label is not None:
            result['Label'] = self.label

        if self.max_score is not None:
            result['MaxScore'] = self.max_score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        result['TopList'] = []
        if self.top_list is not None:
            for k1 in self.top_list:
                result['TopList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')

        self.counter_list = []
        if m.get('CounterList') is not None:
            for k1 in m.get('CounterList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList()
                self.counter_list.append(temp_model.from_map(k1))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.top_list = []
        if m.get('TopList') is not None:
            for k1 in m.get('TopList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The category of the review result. Valid values:
        # 
        # - **live**: The content contains undesirable scenes.
        # - **normal**: normal content.
        self.label = label
        # The score of the image of the category that is indicated by Label.
        self.score = score
        # The position in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the image.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of frames.
        self.count = count
        # The category of the review result. Valid values:
        # 
        # - **live**: The content contains undesirable scenes.
        # - **normal**: normal content.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList] = None,
    ):
        # The average score of the review results.
        self.average_score = average_score
        # The statistics about tag frames.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # - **ad**
        # - **normal**
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # - **block**
        # - **review**
        # - **pass**
        self.suggestion = suggestion
        # The information about the image with the highest score of the category that is indicated by Label.
        self.top_list = top_list

    def validate(self):
        if self.counter_list:
            for v1 in self.counter_list:
                 if v1:
                    v1.validate()
        if self.top_list:
            for v1 in self.top_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_score is not None:
            result['AverageScore'] = self.average_score

        result['CounterList'] = []
        if self.counter_list is not None:
            for k1 in self.counter_list:
                result['CounterList'].append(k1.to_map() if k1 else None)

        if self.label is not None:
            result['Label'] = self.label

        if self.max_score is not None:
            result['MaxScore'] = self.max_score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        result['TopList'] = []
        if self.top_list is not None:
            for k1 in self.top_list:
                result['TopList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')

        self.counter_list = []
        if m.get('CounterList') is not None:
            for k1 in m.get('CounterList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList()
                self.counter_list.append(temp_model.from_map(k1))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.top_list = []
        if m.get('TopList') is not None:
            for k1 in m.get('TopList'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The category of the review result. 
        # 
        # - **ad**
        # - **normal**
        self.label = label
        # The score of the image of the category that is indicated by Label.
        self.score = score
        # The position in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the image.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.score is not None:
            result['Score'] = self.score

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of frames.
        self.count = count
        # The category of the review result. Valid values:
        # 
        # - **ad**
        # - **normal**
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultTextResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        label: str = None,
        scene: str = None,
        score: str = None,
        suggestion: str = None,
        type: str = None,
    ):
        # The text content for review.
        self.content = content
        # The category of the review result. Valid values:
        # 
        # - **spam**
        # - **ad**
        # - **abuse**
        # - **flood**
        # - **contraband**
        # - **meaningless**
        # - **normal**
        self.label = label
        # The review scenario. The value is **antispam**.
        self.scene = scene
        # The score of the image of the category that is indicated by Label.
        self.score = score
        # The recommendation for review results. Valid values:
        # 
        # - **block**
        # - **review**
        # - **pass**
        self.suggestion = suggestion
        # The type of the text. The value is **title**.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.label is not None:
            result['Label'] = self.label

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.score is not None:
            result['Score'] = self.score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultImageResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        result: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult] = None,
        suggestion: str = None,
        type: str = None,
        url: str = None,
    ):
        # The category of the review result. Separate multiple values with commas (,). Valid values:
        # 
        # *   **porn**
        # *   **terrorism**
        # *   **normal**
        self.label = label
        # Details of image review results.
        self.result = result
        # The recommendation for review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
        self.suggestion = suggestion
        # The type of the image. The value is **cover**.
        self.type = type
        # The URL of the image.
        self.url = url

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        scene: str = None,
        score: str = None,
        suggestion: str = None,
    ):
        # The category of the review result.
        # 
        # Valid values if scene is **porn**:
        # 
        # *   **porn**
        # *   **sexy**
        # *   **normal**
        # 
        # Valid values if scene is **terrorism**:
        # 
        # *   **normal**
        # *   **bloody**
        # *   **explosion**
        # *   **outfit**
        # *   **logo**
        # *   **weapon**
        # *   **politics**
        # *   **violence**
        # *   **crowd**
        # *   **parade**
        # *   **carcrash**
        # *   **flag**
        # *   **location**
        # *   **others**
        self.label = label
        # The review scenario. Valid values:
        # 
        # *   **terrorism**
        # *   **porn**
        self.scene = scene
        # The score of the image of the category that is indicated by Label.
        self.score = score
        # The recommendation for review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.score is not None:
            result['Score'] = self.score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultAudioResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        scene: str = None,
        score: str = None,
        suggestion: str = None,
    ):
        # The category of the review result.
        # 
        # *   **normal**
        # *   **spam**
        # *   **ad**
        # *   **politics**
        # *   **terrorism**
        # *   **abuse**
        # *   **porn**
        # *   **flood**
        # *   **contraband**
        # *   **meaningless**
        self.label = label
        # The review scenario. The value is **antispam**.
        self.scene = scene
        # The score.
        self.score = score
        # The recommendation for review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.score is not None:
            result['Score'] = self.score

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

