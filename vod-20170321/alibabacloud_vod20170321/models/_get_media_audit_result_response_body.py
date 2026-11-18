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
        # The moderation result.
        self.media_audit_result = media_audit_result
        # The request ID.
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
        # The moderated content that contains violations. Multiple values are separated by commas (,). Valid values:
        # 
        # - **video**: Video.
        # - **image-cover**: Thumbnail.
        # - **text-title**: Title.
        self.abnormal_modules = abnormal_modules
        # The audio moderation result.
        self.audio_result = audio_result
        # The image moderation result.
        self.image_result = image_result
        # The category of the moderation result. Multiple values are separated by commas (,). Valid values:
        # - **porn**: Pornographic content.
        # - **terrorism**: Terrorist and political content.
        # - **ad**: Image and text violations.
        # - **live**: Inappropriate scenes.
        # - **logo**: Image logos.
        # - **audio**: Audio anti-spam.
        # - **normal**: Normal content.
        self.label = label
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The text moderation result.
        self.text_result = text_result
        # The video moderation result.
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
        green_enhanced_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResult = None,
        label: str = None,
        live_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult = None,
        logo_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult = None,
        porn_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult = None,
        suggestion: str = None,
        terrorism_result: main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult = None,
    ):
        # The ad moderation result.
        self.ad_result = ad_result
        # The GreenEnhanced moderation result.
        self.green_enhanced_result = green_enhanced_result
        # The category of the moderation result. Valid values:
        # - **porn**: Pornographic content.
        # - **terrorism**: Terrorist and political content.
        # - **ad**: Image and text violations.
        # - **live**: Inappropriate scenes.
        # - **logo**: Image logos.
        # - **normal**: Normal content.
        self.label = label
        # The inappropriate content moderation result.
        self.live_result = live_result
        # The logo moderation result.
        self.logo_result = logo_result
        # The pornography moderation result.
        self.porn_result = porn_result
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The moderation result for terrorism and political content.
        self.terrorism_result = terrorism_result

    def validate(self):
        if self.ad_result:
            self.ad_result.validate()
        if self.green_enhanced_result:
            self.green_enhanced_result.validate()
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

        if self.green_enhanced_result is not None:
            result['GreenEnhancedResult'] = self.green_enhanced_result.to_map()

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

        if m.get('GreenEnhancedResult') is not None:
            temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResult()
            self.green_enhanced_result = temp_model.from_map(m.get('GreenEnhancedResult'))

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
        # The average confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.average_score = average_score
        # The categories of terrorism and political content moderation results and the number of video snapshots for each category.
        self.counter_list = counter_list
        # The moderation label for terrorism and political content. Valid values:
        # - **normal**: The content is normal.
        # - **bloody**: The content contains bloody scenes.
        # - **explosion**: The content contains explosions and smoke.
        # - **outfit**: The content contains special outfits.
        # - **logo**: The content contains special logos.
        # - **weapon**: The content contains weapons.
        # - **politics**: The content contains political elements.
        # - **violence**: The content contains violence.
        # - **crowd**: The content contains crowd gatherings.
        # - **parade**: The content contains parades.
        # - **carcrash**: The content contains car crash scenes.
        # - **flag**: The content contains flags.
        # - **location**: The content contains landmarks.
        # - **others**: The content contains other elements.
        self.label = label
        # The maximum confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.max_score = max_score
        # The moderation suggestion for terrorism and political content. Valid values:
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the matched label.
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
        # The moderation label for terrorism and political content. Valid values:
        # - **normal**: The content is normal.
        # - **bloody**: The content contains bloody scenes.
        # - **explosion**: The content contains explosions and smoke.
        # - **outfit**: The content contains special outfits.
        # - **logo**: The content contains special logos.
        # - **weapon**: The content contains weapons.
        # - **politics**: The content contains political elements.
        # - **violence**: The content contains violence.
        # - **crowd**: The content contains crowd gatherings.
        # - **parade**: The content contains parades.
        # - **carcrash**: The content contains car crash scenes.
        # - **flag**: The content contains flags.
        # - **location**: The content contains landmarks.
        # - **others**: The content contains other elements.
        self.label = label
        # The confidence score for the matched label in the video snapshot. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The position of the video snapshot in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the video snapshot.
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
        # The number of video snapshots for the terrorism and political content moderation result.
        self.count = count
        # The moderation label for terrorism and political content. Valid values:
        # - **normal**: The content is normal.
        # - **bloody**: The content contains bloody scenes.
        # - **explosion**: The content contains explosions and smoke.
        # - **outfit**: The content contains special outfits.
        # - **logo**: The content contains special logos.
        # - **weapon**: The content contains weapons.
        # - **politics**: The content contains political elements.
        # - **violence**: The content contains violence.
        # - **crowd**: The content contains crowd gatherings.
        # - **parade**: The content contains parades.
        # - **carcrash**: The content contains car crash scenes.
        # - **flag**: The content contains flags.
        # - **location**: The content contains landmarks.
        # - **others**: The content contains other elements.
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
        # The average confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.average_score = average_score
        # The number of video snapshots for each category in the moderation result.
        self.counter_list = counter_list
        # The pornography moderation result. Valid values:
        # 
        # - **porn**: Pornographic content.
        # - **sexy**: Sexy content.
        # - **normal**: Normal content.
        self.label = label
        # The maximum confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.max_score = max_score
        # The pornography moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the matched label.
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
        # The pornography moderation result. Valid values:
        # 
        # - **porn**: Pornographic content.
        # - **sexy**: Sexy content.
        # - **normal**: Normal content.
        self.label = label
        # The confidence score for the matched label in the video snapshot. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The position of the video snapshot in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the video snapshot.
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
        # The number of video snapshots.
        self.count = count
        # The pornography moderation result. Valid values:
        # 
        # - **porn**: Pornographic content.
        # - **sexy**: Sexy content.
        # - **normal**: Normal content.
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
        # The average confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.average_score = average_score
        # The number of video snapshots for each category in the moderation result.
        self.counter_list = counter_list
        # The category of the logo moderation result. Valid values:
        # - **normal**: Normal content.
        # - **TV**: Regulated logos.
        # - **trademark**: Trademarks.
        self.label = label
        # The maximum confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.max_score = max_score
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the matched label.
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
        # The category of the logo moderation result. Valid values:
        # - **normal**: Normal content.
        # - **TV**: Regulated logos.
        # - **trademark**: Trademarks.
        self.label = label
        # The confidence score for the matched label in the video snapshot. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The position of the video snapshot in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the video snapshot.
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
        # The number of video snapshots.
        self.count = count
        # The category of the logo moderation result. Valid values:
        # - **normal**: Normal content.
        # - **TV**: Regulated logos.
        # - **trademark**: Trademarks.
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
        # The average confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.average_score = average_score
        # The number of video snapshots for each inappropriate content category in the moderation result.
        self.counter_list = counter_list
        # The category of the moderation result. Valid values:
        # - **normal**: Normal content.
        # - **meaningless**: No content in the image, such as a black or white screen.
        # - **PIP**: Picture-in-Picture (PiP).
        # - **smoking**: Smoking.
        # - **drivelive**: Live streaming in a car.
        self.label = label
        # The maximum confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.max_score = max_score
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the matched label.
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
        # The category of the moderation result. Valid values:
        # - **normal**: Normal content.
        # - **meaningless**: No content in the image, such as a black or white screen.
        # - **PIP**: Picture-in-Picture (PiP).
        # - **smoking**: Smoking.
        # - **drivelive**: Live streaming in a car.
        self.label = label
        # The confidence score for the matched label in the video snapshot. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The position of the video snapshot in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the video snapshot.
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
        # The number of video snapshots.
        self.count = count
        # The category of the moderation result. Valid values:
        # - **normal**: Normal content.
        # - **meaningless**: No content in the image, such as a black or white screen.
        # - **PIP**: Picture-in-Picture (PiP).
        # - **smoking**: Smoking.
        # - **drivelive**: Live streaming in a car.
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

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResultTopList] = None,
    ):
        # The average confidence score of the matched frames. This parameter is not returned if no frames are matched.
        self.average_score = average_score
        # The aggregation of violation label counts, including Label for the Green label and Count for the number of matched frames for the label.
        self.counter_list = counter_list
        # The union of matched native Green labels, separated by commas, such as pornographic_adultContent_tii. If no labels are matched, the value is normal.
        self.label = label
        # The maximum confidence score of the matched frames. This parameter is not returned if no frames are matched.
        self.max_score = max_score
        # The image moderation conclusion, which is mapped from frameResult.riskLevel: high is mapped to block, medium or low is mapped to review, and none is mapped to pass.
        self.suggestion = suggestion
        # The details of the matched frames, sorted in descending order of confidence score.
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
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResultCounterList()
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
                temp_model = main_models.GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The moderation result category.
        self.label = label
        # The confidence score of the video snapshot that matches the label.
        self.score = score
        # The timestamp of the video snapshot in the video.
        self.timestamp = timestamp
        # The URL of the video snapshot.
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

class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultGreenEnhancedResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of video snapshots for the corresponding label.
        self.count = count
        # The moderation result label.
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
        # The average confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.average_score = average_score
        # The number of video snapshots for each category in the moderation result.
        self.counter_list = counter_list
        # The category of the ad moderation result. Valid values:
        # - **normal**: Normal content.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Intrusive ads.
        # - **qrcode**: QR codes.
        # - **programCode**: Mini program codes.
        self.label = label
        # The maximum confidence score for the matched label in the video snapshots. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.max_score = max_score
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the matched label.
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
        # The category of the ad moderation result. Valid values:
        # - **normal**: Normal content.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Intrusive ads.
        # - **qrcode**: QR codes.
        # - **programCode**: Mini program codes.
        self.label = label
        # The confidence score for the matched label in the video snapshot. Valid values: `[0, 100]`. The score is accurate to 10 decimal places. The score indicates the probability that the video snapshot belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The position of the video snapshot in the video. Unit: milliseconds.
        self.timestamp = timestamp
        # The URL of the video snapshot.
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
        # The number of video snapshots.
        self.count = count
        # The category of the ad moderation result. Valid values:
        # - **normal**: Normal content.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Intrusive ads.
        # - **qrcode**: QR codes.
        # - **programCode**: Mini program codes.
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
        # The moderated text content.
        self.content = content
        # The category of the moderation result. Valid values:
        # 
        # - **spam**: Spam.
        # - **ad**: Ads.
        # - **abuse**: Abuse.
        # - **flood**: Flooding.
        # - **contraband**: Contraband.
        # - **meaningless**: Meaningless content.
        # - **normal**: Normal content.
        self.label = label
        # The moderation scenario. Fixed value: **antispam**.
        self.scene = scene
        # The confidence score for the matched label in the text snapshot. Valid values: `[0, 100]`. The score indicates the probability that the text belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The text categorization. Valid value: **title** (title).
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
        # The category of the image moderation result. Multiple values are separated by commas (,). Valid values:
        # 
        # - **porn**: Pornographic content.
        # - **terrorism**: Terrorist and political content.
        # - **ad**: Image and text violations.
        # - **live**: Inappropriate scenes.
        # - **logo**: Image logos.
        # - **normal**: Normal content.
        self.label = label
        # The details of the image moderation result.
        self.result = result
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The image category. Valid value: **cover** (thumbnail).
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
        # The category of the moderation result.
        # 
        # When the scene is **porn**, valid values are:
        # 
        # - **porn**: Pornographic content.
        # - **sexy**: Sexy content.
        # - **normal**: Normal content.
        # 
        # When the scene is **terrorism**, valid values are:
        # 
        # - **normal**: Normal content.
        # - **bloody**: Bloody content.
        # - **explosion**: Explosions and smoke.
        # - **outfit**: Special outfits.
        # - **logo**: Special logos.
        # - **weapon**: Weapons.
        # - **politics**: Political content.
        # - **violence**: Violence.
        # - **crowd**: Crowds.
        # - **parade**: Parades.
        # - **carcrash**: Car crashes.
        # - **flag**: Flags.
        # - **location**: Landmarks.
        # - **others**: Others.
        # 
        # When the scene is **ad**, valid values are:
        # 
        # - **normal**: Normal content.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Intrusive ads.
        # - **qrcode**: QR codes.
        # - **programCode**: Mini program codes.
        # 
        # When the scene is **live**, valid values are:
        # - **normal**: Normal content.
        # - **meaningless**: No content in the image, such as a black or white screen.
        # - **PIP**: Picture-in-Picture (PiP).
        # - **smoking**: Smoking.
        # - **drivelive**: Live streaming in a car.
        # 
        # When the scene is **logo**, valid values are:
        # - **normal**: Normal content.
        # - **TV**: Regulated logos.
        # - **trademark**: Trademarks.
        self.label = label
        # The moderation scenario. Valid values:
        # 
        # - **porn**: Pornography detection.
        # - **terrorism**: Terrorist and political content detection.
        # - **ad**: Image and text violation detection.
        # - **live**: Inappropriate scene detection.
        # - **logo**: Image logo detection.
        self.scene = scene
        # The confidence score for the matched label in the image. Valid values: `[0, 100]`. The score indicates the probability that the image belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
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
        # The category of the moderation result. Valid values:
        # 
        # - **normal**: Normal content.
        # - **spam**: Spam.
        # - **ad**: Ads.
        # - **politics**: Political content.
        # - **terrorism**: Terrorist content.
        # - **abuse**: Abuse.
        # - **porn**: Pornographic content.
        # - **flood**: Flooding.
        # - **contraband**: Contraband.
        # - **meaningless**: Meaningless content.
        self.label = label
        # The moderation scenario. Fixed value: **antispam**.
        self.scene = scene
        # The confidence score for the matched label in the audio. Valid values: `[0, 100]`. The score indicates the probability that the audio belongs to the corresponding category. A higher score indicates higher accuracy.
        self.score = score
        # The moderation suggestion. Valid values:
        # 
        # - **block**: The content is blocked.
        # - **review**: The content requires manual review.
        # - **pass**: The content passes the moderation.
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

