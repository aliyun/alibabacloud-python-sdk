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
        # The information about the intelligent review job.
        self.media_audit_job = media_audit_job
        # The ID of the request.
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
        # The error code. This parameter is returned if the value of Status is fail.
        self.code = code
        # The time when the job is complete. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the job started to run. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The job result.
        self.data = data
        # The ID of the job.
        self.job_id = job_id
        # The ID of the video.
        self.media_id = media_id
        # The error message. This parameter is returned if the value of Status is fail.
        self.message = message
        # The status of the job. Valid values:
        # 
        # *   **success**: The job is successful.
        # *   **fail**: The job failed.
        # *   **init**: The job is being initialized.
        # *   **Processing**: The job is in progress.
        self.status = status
        # The type of the job. The value is AIMediaAudit.
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
        # The content that violates the regulations. Separate multiple values with commas (,). Valid values:
        # 
        # *   **video**: the video.
        # *   **image-cover**: the cover.
        # *   **text-title**: the title.
        self.abnormal_modules = abnormal_modules
        # The results of audio review.
        self.audio_result = audio_result
        # The results of image review.
        self.image_result = image_result
        # The category of the review result. Multiple values are separated by commas (,). Valid values:
        # 
        # *   **porn**: pornographic content
        # *   **terrorism**: terrorist or politically sensitive content
        # *   **ad**: ad violation
        # *   **live**: undesirable scene
        # *   **logo**: logo
        # *   **audio**: audio anti-spam
        # *   **normal**: normal content
        self.label = label
        # The recommendation for review results. Valid values:
        # 
        # *   **block**: The content violates the regulations.
        # *   **review**: The content may violate the regulations.
        # *   **pass**: The content passes the review.
        self.suggestion = suggestion
        # The text moderation results.
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
        label: str = None,
        live_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult = None,
        logo_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult = None,
        porn_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult = None,
        suggestion: str = None,
        terrorism_result: main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult = None,
    ):
        # The results of ad review.
        self.ad_result = ad_result
        # The category of the review result. Valid values:
        # 
        # *   **porn**: pornographic content
        # *   **terrorism**: terrorist or politically sensitive content
        # *   **ad**: ad violation
        # *   **live**: undesirable scene
        # *   **logo**: logo
        # *   **normal**
        self.label = label
        # The results of undesired content review.
        self.live_result = live_result
        # The results of logo review.
        self.logo_result = logo_result
        # The results of pornographic content review.
        self.porn_result = porn_result
        # The recommendation for video review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
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
            temp_model = main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult()
            self.ad_result = temp_model.from_map(m.get('AdResult'))

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
        # The average score of the snapshots of the category that is indicated by Label. Valid values: `[0, 100]`. The value is accurate to 10 decimal places. The score is representative of the confidence.
        self.average_score = average_score
        # The categories of terrorist content review results and the number of video snapshots in each category.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
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
        # The highest score of the snapshot of the category that is indicated by Label. Valid values: `[0, 100]`. The value is accurate to 10 decimal places. The score is representative of the confidence.
        self.max_score = max_score
        # The recommendation for terrorist content review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
        self.suggestion = suggestion
        # The information about the snapshot that has the highest score in the category.
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
        # The results of terrorist content review. Valid values:
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
        # The score of the snapshot in the category that is indicated by Label. Valid values: `[0, 100]`. The value is accurate to 10 decimal places. The score is representative of the confidence.
        self.score = score
        # The timestamp of the snapshot in the video. Unit: milliseconds.
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
        # The results of terrorist content review. Valid values:
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
        # The average score of the snapshots of the category that is indicated by Label. Valid values: `[0, 100]`. The value is accurate to 10 decimal places. The score is representative of the confidence.
        self.average_score = average_score
        # The number of snapshots of each category in the review result.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # *   **porn**
        # *   **sexy**
        # *   **normal**
        self.label = label
        # The highest score of the snapshot of the category that is indicated by Label. Valid values: `[0, 100]`. The value is accurate to 10 decimal places. The score is representative of the confidence.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # *   **block**: The content violates the regulations.
        # *   **review**: The content may violate the regulations.
        # *   **pass**: The content passes the review.
        self.suggestion = suggestion
        # The information about the snapshot that has the highest score in the category.
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
        # The results of pornographic content review. Valid values:
        # 
        # *   **porn**
        # *   **sexy**
        # *   **normal**
        self.label = label
        # The score of the snapshot in the category that is indicated by Label. Valid values: `[0, 100]`. The value is accurate to 10 decimal places. The score is representative of the confidence.
        self.score = score
        # The timestamp of the snapshot in the video. Unit: milliseconds.
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
        # The results of pornographic content review. Valid values:
        # 
        # *   **porn**
        # *   **sexy**
        # *   **normal**
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
        # The average score of the snapshots in the category indicated by Label.
        self.average_score = average_score
        # The categories of the review results and the number of video snapshots in each category.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # *   **normal**: normal content
        # *   **TV**: controlled TV station logo
        # *   **trademark**: trademark
        self.label = label
        # The highest score of the snapshot of the category that is indicated by Label.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # *   **block**: The content violates the regulations.
        # *   **review**: The content may violate the regulations.
        # *   **pass**: The content passes the review.
        self.suggestion = suggestion
        # The information about the snapshot that has the highest score in the category.
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
        # The category of the review result. Valid values:
        # 
        # *   **normal**: normal content
        # *   **TV**: controlled TV station logo
        # *   **trademark**: trademark
        self.label = label
        # The score of the snapshot in the category that is indicated by Label.
        self.score = score
        # The timestamp of the snapshot in the video. Unit: milliseconds.
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
        # The category of the review result. Valid values:
        # 
        # *   **normal**: normal content
        # *   **TV**: controlled TV station logo
        # *   **trademark**: trademark
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
        # The average score of the review results.
        self.average_score = average_score
        # The categories of the review results and the number of video snapshots in each category.
        self.counter_list = counter_list
        # The category of the review result. Valid values:
        # 
        # *   **normal**: normal content
        # *   **meaningless**: meaningless content, such as a black or white screen.
        # *   **PIP**: picture-in-picture
        # *   **smoking**: smoking
        # *   **drivelive**: live broadcasting in a running vehicle
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # *   **block**: The content violates the regulations.
        # *   **review**: The content may violate the regulations.
        # *   **pass**: The content passes the review.
        self.suggestion = suggestion
        # The information about the snapshot that has the highest score in the category.
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
        # The category of the review result. Valid values:
        # 
        # *   **normal**: normal content
        # *   **meaningless**: meaningless content, such as a black or white screen.
        # *   **PIP**: picture-in-picture
        # *   **smoking**: smoking
        # *   **drivelive**: live broadcasting in a running vehicle
        self.label = label
        # The score of the snapshot in the category that is indicated by Label.
        self.score = score
        # The timestamp of the snapshot in the video. Unit: milliseconds.
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
        # The category of the review result. Valid values:
        # 
        # *   **normal**: normal content
        # *   **meaningless**: meaningless content, such as a black or white screen.
        # *   **PIP**: picture-in-picture
        # *   **smoking**: smoking
        # *   **drivelive**: live broadcasting in a running vehicle
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
        # The average score of the review results.
        self.average_score = average_score
        # The number of snapshots of each category in the review result.
        self.counter_list = counter_list
        # The categories of the ad review results. Valid values:
        # 
        # *   **normal**: normal content
        # *   **ad**: other ads
        # *   **politics**: political content
        # *   **porn**: pornographic content
        # *   **abuse**: abuse
        # *   **terrorism**: terrorist content
        # *   **contraband**: prohibited content
        # *   **spam**: spam content
        # *   **npx**: illegal ad
        # *   **qrcode**: QR code
        # *   **programCode**: mini program code
        self.label = label
        # The highest review score.
        self.max_score = max_score
        # The recommendation for review results. Valid values:
        # 
        # *   **block**: The content violates the regulations.
        # *   **review**: The content may violate the regulations.
        # *   **pass**: The content passes the review.
        self.suggestion = suggestion
        # The information about the snapshot that has the highest score in the category.
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
        # The categories of the ad review results. Valid values:
        # 
        # *   **normal**: normal content
        # *   **ad**: other ads
        # *   **politics**: political content
        # *   **porn**: pornographic content
        # *   **abuse**: abuse
        # *   **terrorism**: terrorist content
        # *   **contraband**: prohibited content
        # *   **spam**: spam content
        # *   **npx**: illegal ad
        # *   **qrcode**: QR code
        # *   **programCode**: mini program code
        self.label = label
        # The score of the snapshot in the category that is indicated by Label.
        self.score = score
        # The timestamp of the snapshot in the video. Unit: milliseconds.
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
        # The categories of the ad review results. Valid values:
        # 
        # *   **normal**: normal content
        # *   **ad**: other ads
        # *   **politics**: political content
        # *   **porn**: pornographic content
        # *   **abuse**: abuse
        # *   **terrorism**: terrorist content
        # *   **contraband**: prohibited content
        # *   **spam**: spam content
        # *   **npx**: illegal ad
        # *   **qrcode**: QR code
        # *   **programCode**: mini program code
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
        # The category of the review result. Valid values:
        # 
        # *   **spam**: spam content
        # *   **ad**: ads
        # *   **abuse**: abuse
        # *   **flood**: excessive junk content
        # *   **contraband**: prohibited content
        # *   **meaningless**: meaningless content
        # *   **normal**: normal content
        self.label = label
        # The review scenario. The value is **antispam**.
        self.scene = scene
        # The score of the image of the category that is indicated by Label. Valid values: `[0, 100]`. The score is representative of the confidence.
        self.score = score
        # The recommendation for review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        result: List[main_models.GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult] = None,
        suggestion: str = None,
        type: str = None,
        url: str = None,
    ):
        # The categories of the image review results. Multiple values are separated by commas (,). Valid values:
        # 
        # *   **porn**: pornographic content
        # *   **terrorism**: terrorist or politically sensitive content
        # *   **ad**: ad violation
        # *   **live**: undesirable scene
        # *   **logo**: logo
        # *   **normal**: normal content
        self.label = label
        # Details of image review results.
        self.result = result
        # The recommendation for review results. Valid values:
        # 
        # *   **block**
        # *   **review**
        # *   **pass**
        self.suggestion = suggestion
        # The type of the image. Valid value: **cover**.
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
        # 
        # Valid values if scene is **ad**:
        # 
        # *   **normal**: normal content
        # *   **ad**: ads
        # *   **politics**: political content
        # *   **porn**: pornographic content
        # *   **abuse**: verbal abuse
        # *   **terrorism**: terrorist content
        # *   **contraband**: prohibited content
        # *   **spam**: spam content
        # *   **npx**: illegal ad
        # *   **qrcode**: QR code
        # *   **programCode**: mini program code
        # 
        # Valid values if scene is **live**:
        # 
        # *   **normal**: normal content
        # *   **meaningless**: meaningless content, such as a black or white screen.
        # *   **PIP**: picture-in-picture
        # *   **smoking**: smoking
        # *   **drivelive**: live broadcasting in a running vehicle
        # 
        # Valid values if scene is **logo**:
        # 
        # *   **normal**: normal content
        # *   **TV**: controlled TV station logo
        # *   **trademark**: trademark
        self.label = label
        # The review scenario. Valid values:
        # 
        # *   **porn**: pornographic content
        # *   **terrorism**: terrorist or politically sensitive content
        # *   **ad**: ad violation
        # *   **live**: undesirable scene
        # *   **logo**: logo
        self.scene = scene
        # The score of the image of the category that is indicated by Label. Valid values: `[0, 100]`. The score is representative of the confidence.
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

class GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult(DaraModel):
    def __init__(
        self,
        label: str = None,
        scene: str = None,
        score: str = None,
        suggestion: str = None,
    ):
        # The category of the review result.
        # 
        # *   **normal**: normal content
        # *   **spam**: spam
        # *   **ad**: ads
        # *   **politics**: political content
        # *   **terrorism**: terrorist content
        # *   **abuse**: abuse
        # *   **porn**: pornographic content.
        # *   **flood**: excessive junk content
        # *   **contraband**: prohibited content
        # *   **meaningless**: meaningless content
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

