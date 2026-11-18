# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetAIMediaAuditJobResponseBody(DaraModel):
    def __init__(
        self,
        media_audit_job: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJob = None,
        request_id: str = None,
    ):
        # The automated review job information.
        self.media_audit_job = media_audit_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_audit_job:
            self.media_audit_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_audit_job is not None:
            result['MediaAuditJob'] = self.media_audit_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaAuditJob') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJob()
            self.media_audit_job = temp_model.from_map(m.get('MediaAuditJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        complete_time: str = None,
        creation_time: str = None,
        data: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobData = None,
        job_id: str = None,
        media_id: str = None,
        message: str = None,
        status: str = None,
        type: str = None,
    ):
        # The job error code. Check this field when the job status is fail.
        self.code = code
        # The end time of the job. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.complete_time = complete_time
        # The start time of the job. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.creation_time = creation_time
        # The job result data.
        self.data = data
        # The job ID.
        self.job_id = job_id
        # The video ID.
        self.media_id = media_id
        # The job error message. Check this field when the job status is fail.
        self.message = message
        # The job status. Valid values:
        # 
        # - **success**: Succeeded.
        # - **fail**: Failed.
        # - **init**: Initialized.
        # - **processing**: Processing.
        self.status = status
        # The job type. Currently, only automated review is supported.
        self.type = type

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

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.message is not None:
            result['Message'] = self.message

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Data') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobData(DaraModel):
    def __init__(
        self,
        abnormal_modules: str = None,
        audio_result: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult] = None,
        image_result: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult] = None,
        label: str = None,
        suggestion: str = None,
        text_result: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult] = None,
        video_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult = None,
    ):
        # The reviewed content that contains violations. Multiple values are separated by commas (,). Valid values:
        # 
        # - **video**: Video.
        # - **image-cover**: Thumbnail.
        # - **text-title**: Title.
        self.abnormal_modules = abnormal_modules
        # The audio review result.
        self.audio_result = audio_result
        # The image review result.
        self.image_result = image_result
        # The review result category. Multiple values are separated by commas (,). Valid values:
        # 
        # - **porn**: Pornographic content.
        # - **terrorism**: Terrorist and political content.
        # - **ad**: Image and text violation.
        # - **live**: Undesirable scene.
        # - **logo**: Image logo.
        # - **audio**: Audio anti-spam.
        # - **normal**: Normal.
        self.label = label
        # The review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
        self.suggestion = suggestion
        # The text review result.
        self.text_result = text_result
        # The video review result.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult()
                self.audio_result.append(temp_model.from_map(k1))

        self.image_result = []
        if m.get('ImageResult') is not None:
            for k1 in m.get('ImageResult'):
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult()
                self.image_result.append(temp_model.from_map(k1))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        self.text_result = []
        if m.get('TextResult') is not None:
            for k1 in m.get('TextResult'):
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult()
                self.text_result.append(temp_model.from_map(k1))

        if m.get('VideoResult') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult()
            self.video_result = temp_model.from_map(m.get('VideoResult'))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult(DaraModel):
    def __init__(
        self,
        ad_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult = None,
        green_enhanced_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResult = None,
        label: str = None,
        live_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult = None,
        logo_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult = None,
        porn_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult = None,
        suggestion: str = None,
        terrorism_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult = None,
    ):
        # The ad review result.
        self.ad_result = ad_result
        # The GreenEnhanced moderation result.
        self.green_enhanced_result = green_enhanced_result
        # The review result category. Valid values:
        # - **porn**: Pornographic content.
        # - **terrorism**: Terrorist and political content.
        # - **ad**: Image and text violation.
        # - **live**: Undesirable scene.
        # - **logo**: Image logo.
        # - **normal**: Normal.
        self.label = label
        # The harmful content moderation result.
        self.live_result = live_result
        # The logo moderation result.
        self.logo_result = logo_result
        # The pornography detection result.
        self.porn_result = porn_result
        # The video review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
        self.suggestion = suggestion
        # The terrorist and political content review result.
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
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult()
            self.ad_result = temp_model.from_map(m.get('AdResult'))

        if m.get('GreenEnhancedResult') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResult()
            self.green_enhanced_result = temp_model.from_map(m.get('GreenEnhancedResult'))

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LiveResult') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult()
            self.live_result = temp_model.from_map(m.get('LiveResult'))

        if m.get('LogoResult') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult()
            self.logo_result = temp_model.from_map(m.get('LogoResult'))

        if m.get('PornResult') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult()
            self.porn_result = temp_model.from_map(m.get('PornResult'))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('TerrorismResult') is not None:
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult()
            self.terrorism_result = temp_model.from_map(m.get('TerrorismResult'))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList] = None,
    ):
        # The average score of the video snapshots that hit the label. Valid values: `[0, 100]`. The precision is 10 decimal places. The score indicates the probability that the snapshot belongs to the corresponding label category. A higher score indicates higher accuracy.
        self.average_score = average_score
        # The categories of the terrorist and political content review results and the number of video snapshots for each category.
        self.counter_list = counter_list
        # The terrorist and political content review result. Valid values:
        # 
        # - **normal**: Normal.
        # - **bloody**: Bloody.
        # - **explosion**: Explosion and smoke.
        # - **outfit**: Special outfit.
        # - **logo**: Special logo.
        # - **weapon**: Weapon.
        # - **politics**: Political content.
        # - **violence**: Violence.
        # - **crowd**: Crowd.
        # - **parade**: Parade.
        # - **carcrash**: Car crash.
        # - **flag**: Flag.
        # - **location**: Landmark.
        # - **others**: Others.
        self.label = label
        # The highest score of the video snapshots that hit the label. Valid values: `[0, 100]`. The precision is 10 decimal places. The score indicates the probability that the snapshot belongs to the corresponding label category. A higher score indicates higher accuracy.
        self.max_score = max_score
        # The terrorist and political content review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the hit label.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList()
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The terrorist and political content review result. Valid values:
        # 
        # - **normal**: Normal.
        # - **bloody**: Bloody.
        # - **explosion**: Explosion and smoke.
        # - **outfit**: Special outfit.
        # - **logo**: Special logo.
        # - **weapon**: Weapon.
        # - **politics**: Political content.
        # - **violence**: Violence.
        # - **crowd**: Crowd.
        # - **parade**: Parade.
        # - **carcrash**: Car crash.
        # - **flag**: Flag.
        # - **location**: Landmark.
        # - **others**: Others.
        self.label = label
        # The score of the video snapshot that hits the label. Valid values: `[0, 100]`. The precision is 10 decimal places. The score indicates the probability that the snapshot belongs to the corresponding label category. A higher score indicates higher accuracy.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of video snapshots.
        self.count = count
        # The terrorist and political content review result. Valid values:
        # - **normal**: Normal.
        # - **bloody**: Bloody.
        # - **explosion**: Explosion and smoke.
        # - **outfit**: Special outfit.
        # - **logo**: Special logo.
        # - **weapon**: Weapon.
        # - **politics**: Political content.
        # - **violence**: Violence.
        # - **crowd**: Crowd.
        # - **parade**: Parade.
        # - **carcrash**: Car crash.
        # - **flag**: Flag.
        # - **location**: Landmark.
        # - **others**: Others.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList] = None,
    ):
        # The average score of the video snapshots that hit the label. Valid values: `[0, 100]`. The precision is 10 decimal places. The score indicates the probability that the snapshot belongs to the corresponding label category. A higher score indicates higher accuracy.
        self.average_score = average_score
        # The categories of the review results and the number of video snapshots for each category.
        self.counter_list = counter_list
        # The pornography detection result. Valid values:
        # 
        # - **porn**: Pornographic.
        # - **sexy**: Sexy.
        # - **normal**: Normal.
        self.label = label
        # The highest score of the video snapshots that hit the label. Valid values: `[0, 100]`. The precision is 10 decimal places. The score indicates the probability that the snapshot belongs to the corresponding label category. A higher score indicates higher accuracy.
        self.max_score = max_score
        # The pornography detection suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the hit label.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList()
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The pornography detection result. Valid values:
        # 
        # - **porn**: Pornographic.
        # - **sexy**: Sexy.
        # - **normal**: Normal.
        self.label = label
        # The score of the video snapshot that hits the label. Valid values: `[0, 100]`. The precision is 10 decimal places. The score indicates the probability that the snapshot belongs to the corresponding label category. A higher score indicates higher accuracy.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of video snapshots.
        self.count = count
        # The pornography detection result. Valid values:
        # 
        # - **porn**: Pornographic.
        # - **sexy**: Sexy.
        # - **normal**: Normal.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList] = None,
    ):
        # The average score of the video snapshots that hit the label.
        self.average_score = average_score
        # The moderation categories and the number of video snapshots for each category.
        self.counter_list = counter_list
        # The logo moderation category. Valid values:
        # - **normal**: normal
        # - **TV**: the image contains a regulated logo
        # - **trademark**: the image contains a trademark
        self.label = label
        # The highest score of the video snapshots that hit the label.
        self.max_score = max_score
        # The logo moderation suggestion. Valid values:
        # - **block**: The content violates regulations.
        # - **review**: The content is suspected of violating regulations.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the hit label.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList()
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The logo moderation category. Valid values:
        # - **normal**: normal
        # - **TV**: the image contains a regulated logo
        # - **trademark**: the image contains a trademark
        self.label = label
        # The score of the video snapshot that hits the label.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of video snapshots.
        self.count = count
        # The logo moderation category. Valid values:
        # - **normal**: normal
        # - **TV**: the image contains a regulated logo
        # - **trademark**: the image contains a trademark
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList] = None,
    ):
        # The average score of the moderation result.
        self.average_score = average_score
        # The moderation categories and the number of video snapshots for each category.
        self.counter_list = counter_list
        # The moderation category. Valid values:
        # - **normal**: normal
        # - **meaningless**: the image contains no content, such as a black or white screen
        # - **PIP**: Picture-in-Picture (PiP)
        # - **smoking**: smoking
        # - **drivelive**: live streaming inside a vehicle
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The moderation suggestion. Valid values:
        # - **block**: The content violates regulations.
        # - **review**: The content is suspected of violating regulations.
        # - **pass**: The content passes the moderation.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the hit label.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList()
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The moderation category. Valid values:
        # - **normal**: normal
        # - **meaningless**: the image contains no content, such as a black or white screen
        # - **PIP**: Picture-in-Picture (PiP)
        # - **smoking**: smoking
        # - **drivelive**: live streaming inside a vehicle
        self.label = label
        # The score of the video snapshot that hits the label.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of video snapshots.
        self.count = count
        # The moderation category. Valid values:
        # - **normal**: normal
        # - **meaningless**: the image contains no content, such as a black or white screen
        # - **PIP**: Picture-in-Picture (PiP)
        # - **smoking**: smoking
        # - **drivelive**: live streaming inside a vehicle
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResultTopList] = None,
    ):
        # The average confidence score of the hit frames. This parameter is not returned if no frames are hit.
        self.average_score = average_score
        # The aggregated count of violation labels, including Label (the Green label) and Count (the number of frames that hit the label).
        self.counter_list = counter_list
        # The union of hit Green native labels, separated by commas, such as pornographic_adultContent_tii. If no labels are hit, the value is normal.
        self.label = label
        # The highest confidence score of the hit frames. This parameter is not returned if no frames are hit.
        self.max_score = max_score
        # The image moderation conclusion, which is mapped from frameResult.riskLevel: high to block, medium or low to review, and none to pass.
        self.suggestion = suggestion
        # The details of the hit frames, sorted in descending order of confidence score.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResultCounterList()
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The moderation category.
        self.label = label
        # The confidence score of the video snapshot that hits the label.
        self.score = score
        # The position of the video snapshot in the video.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultGreenEnhancedResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of video frames that correspond to the label.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult(DaraModel):
    def __init__(
        self,
        average_score: str = None,
        counter_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList] = None,
        label: str = None,
        max_score: str = None,
        suggestion: str = None,
        top_list: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList] = None,
    ):
        # The average score of the ad review result.
        self.average_score = average_score
        # The categories of the review results and the number of video snapshots for each category.
        self.counter_list = counter_list
        # The ad review result category. Valid values:
        # - **normal**: Normal.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Nuisance ad.
        # - **qrcode**: QR code included.
        # - **programCode**: Mini program code included.
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
        self.suggestion = suggestion
        # The information about the video snapshots with the highest scores for the hit label.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList()
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList()
                self.top_list.append(temp_model.from_map(k1))

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList(DaraModel):
    def __init__(
        self,
        label: str = None,
        score: str = None,
        timestamp: str = None,
        url: str = None,
    ):
        # The ad review result category. Valid values:
        # - **normal**: Normal.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Nuisance ad.
        # - **qrcode**: QR code included.
        # - **programCode**: Mini program code included.
        self.label = label
        # The score of the video snapshot that hits the label.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
    ):
        # The number of video snapshots.
        self.count = count
        # The ad review result category. Valid values:
        # - **normal**: Normal.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Nuisance ad.
        # - **qrcode**: QR code included.
        # - **programCode**: Mini program code included.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        label: str = None,
        scene: str = None,
        score: str = None,
        suggestion: str = None,
        type: str = None,
    ):
        # The text content.
        self.content = content
        # The review result category. Valid values:
        # - **spam**: Spam content.
        # - **ad**: Ad.
        # - **abuse**: Abuse.
        # - **flood**: Flooding.
        # - **contraband**: Contraband.
        # - **meaningless**: Meaningless.
        # - **normal**: Normal.
        self.label = label
        # The review scene. Fixed value: **antispam**.
        self.scene = scene
        # The score of the image that hits the label. Valid values: `[0, 100]`. The score indicates the probability that the image belongs to the corresponding label category. A higher score indicates higher accuracy.
        self.score = score
        # The review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        result: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult] = None,
        suggestion: str = None,
        type: str = None,
        url: str = None,
    ):
        # The image review result category. Multiple values are separated by commas (,). Valid values:
        # 
        # - **porn**: Pornographic content.
        # - **terrorism**: Terrorist and political content.
        # - **ad**: Image and text violation.
        # - **live**: Undesirable scene.
        # - **logo**: Image logo.
        # - **normal**: Normal.
        self.label = label
        # The image review result details.
        self.result = result
        # The review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
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
                temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        scene: str = None,
        score: str = None,
        suggestion: str = None,
    ):
        # The review result category.
        # 
        # When the scene is **porn**, valid values:
        # 
        # - **porn**: Pornographic.
        # - **sexy**: Sexy.
        # - **normal**: Normal.
        # 
        # When the scene is **terrorism**, valid values:
        # 
        # - **normal**: Normal.
        # - **bloody**: Bloody.
        # - **explosion**: Explosion and smoke.
        # - **outfit**: Special outfit.
        # - **logo**: Special logo.
        # - **weapon**: Weapon.
        # - **politics**: Political content.
        # - **violence**: Violence.
        # - **crowd**: Crowd.
        # - **parade**: Parade.
        # - **carcrash**: Car crash.
        # - **flag**: Flag.
        # - **location**: Landmark.
        # - **others**: Others.
        # 
        # When the scene is **ad**, valid values:
        # 
        # - **normal**: Normal.
        # - **ad**: Other ads.
        # - **politics**: Text containing political content.
        # - **porn**: Text containing pornographic content.
        # - **abuse**: Text containing abusive content.
        # - **terrorism**: Text containing terrorist content.
        # - **contraband**: Text containing contraband content.
        # - **spam**: Text containing other spam content.
        # - **npx**: Nuisance ad.
        # - **qrcode**: QR code included.
        # - **programCode**: Mini program code included.
        # 
        # When the scene is **live**, valid values:
        # - **normal**: Normal.
        # - **meaningless**: No content in the image, such as a black or white screen.
        # - **PIP**: Picture-in-Picture (PiP).
        # - **smoking**: Smoking.
        # - **drivelive**: In-car live streaming.
        # 
        # When the scene is **logo**, valid values:
        # - **normal**: Normal.
        # - **TV**: Regulated logo included.
        # - **trademark**: Trademark included.
        self.label = label
        # The review scene. Valid values:
        # 
        # - **porn**: Pornography detection.
        # - **terrorism**: Terrorist and political content detection.
        # - **ad**: Image and text violation detection.
        # - **live**: Undesirable scene detection.
        # - **logo**: Image logo detection.
        self.scene = scene
        # The score of the image that hits the label. Valid values: `[0, 100]`. The score indicates the probability that the image belongs to the corresponding label category. A higher score indicates higher accuracy.
        self.score = score
        # The review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        scene: str = None,
        score: str = None,
        suggestion: str = None,
    ):
        # The review result category. Valid values:
        # 
        # - **normal**: Normal.
        # - **spam**: Spam content.
        # - **ad**: Ad.
        # - **politics**: Political content.
        # - **terrorism**: Terrorist content.
        # - **abuse**: Abuse.
        # - **porn**: Pornographic content.
        # - **flood**: Flooding.
        # - **contraband**: Contraband.
        # - **meaningless**: Meaningless.
        self.label = label
        # The review scene. Fixed value: **antispam**.
        self.scene = scene
        # The result score.
        self.score = score
        # The review suggestion. Valid values:
        # 
        # - **block**: Violation.
        # - **review**: Suspected violation.
        # - **pass**: Passed.
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

