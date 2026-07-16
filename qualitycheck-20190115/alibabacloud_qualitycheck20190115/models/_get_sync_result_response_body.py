# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetSyncResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.GetSyncResultResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        # Result code. A value of 200 indicates success. Any other value indicates failure. The caller can use this field to determine the cause of failure.
        self.code = code
        # Total number of entries.
        self.count = count
        # Query result.
        self.data = data
        # Error details when an error occurs; "successful" when the operation succeeded.
        self.message = message
        # Page number
        self.page_number = page_number
        # Number of entries per page.
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Internal field. Ignore it.
        self.result_count_id = result_count_id
        # Indicates whether the request succeeded. The caller can use this field to determine the request status: true indicates success; false or null indicates failure.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSyncResultResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSyncResultResponseBodyData(DaraModel):
    def __init__(
        self,
        agent: main_models.GetSyncResultResponseBodyDataAgent = None,
        asr_result: List[main_models.GetSyncResultResponseBodyDataAsrResult] = None,
        comments: str = None,
        create_time: str = None,
        error_message: str = None,
        hit_result: List[main_models.GetSyncResultResponseBodyDataHitResult] = None,
        recording: main_models.GetSyncResultResponseBodyDataRecording = None,
        resolver: str = None,
        review_result: int = None,
        review_status: int = None,
        reviewer: str = None,
        score: int = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # Agent information
        self.agent = agent
        # Transcription result (dialogue text)
        self.asr_result = asr_result
        # Review comments.
        self.comments = comments
        # Job Creation Time.
        self.create_time = create_time
        # When status is neither 0 nor 1, this field indicates the Error Details.
        self.error_message = error_message
        # Rule hit result.
        self.hit_result = hit_result
        # Recording file information
        self.recording = recording
        # The quality inspector who actually reviewed the task.
        self.resolver = resolver
        # Review accuracy. Possible values: 0 (fault); 1 (correct); 2 (partially correct); 3 (pending review).
        self.review_result = review_result
        # Review status; possible values: 0 (not reviewed); 1 (reviewed).
        self.review_status = review_status
        # Username of the assigned quality inspector.
        self.reviewer = reviewer
        # Quality inspection score, with a maximum of 100.
        self.score = score
        # Current job status. Possible values: 0 (not completed); 1 (completed). The caller can use this field to determine whether the job is complete. Values other than 0 or 1 indicate an error; see the errorMessage field for Error Details.
        self.status = status
        # Job ID.
        self.task_id = task_id
        # Internal field. Ignore it.
        self.task_name = task_name

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.asr_result:
            for v1 in self.asr_result:
                 if v1:
                    v1.validate()
        if self.hit_result:
            for v1 in self.hit_result:
                 if v1:
                    v1.validate()
        if self.recording:
            self.recording.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        result['AsrResult'] = []
        if self.asr_result is not None:
            for k1 in self.asr_result:
                result['AsrResult'].append(k1.to_map() if k1 else None)

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['HitResult'] = []
        if self.hit_result is not None:
            for k1 in self.hit_result:
                result['HitResult'].append(k1.to_map() if k1 else None)

        if self.recording is not None:
            result['Recording'] = self.recording.to_map()

        if self.resolver is not None:
            result['Resolver'] = self.resolver

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status

        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer

        if self.score is not None:
            result['Score'] = self.score

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.GetSyncResultResponseBodyDataAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        self.asr_result = []
        if m.get('AsrResult') is not None:
            for k1 in m.get('AsrResult'):
                temp_model = main_models.GetSyncResultResponseBodyDataAsrResult()
                self.asr_result.append(temp_model.from_map(k1))

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.hit_result = []
        if m.get('HitResult') is not None:
            for k1 in m.get('HitResult'):
                temp_model = main_models.GetSyncResultResponseBodyDataHitResult()
                self.hit_result.append(temp_model.from_map(k1))

        if m.get('Recording') is not None:
            temp_model = main_models.GetSyncResultResponseBodyDataRecording()
            self.recording = temp_model.from_map(m.get('Recording'))

        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')

        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

class GetSyncResultResponseBodyDataRecording(DaraModel):
    def __init__(
        self,
        business: str = None,
        call_id: str = None,
        call_time: str = None,
        call_type: int = None,
        callee: str = None,
        caller: str = None,
        data_set_name: str = None,
        duration: int = None,
        duration_audio: int = None,
        id: str = None,
        name: str = None,
        primary_id: str = None,
        remark_1: str = None,
        remark_2: str = None,
        remark_3: str = None,
        url: str = None,
    ):
        # Line-of-business name.
        self.business = business
        # Call ID.
        self.call_id = call_id
        # Recording generation UNIX timestamp, accurate to milliseconds.
        self.call_time = call_time
        # Call type:  
        # - 1: Outgoing call  
        # - 3: Incoming call
        self.call_type = call_type
        # Callee number.
        self.callee = callee
        # Caller number.
        self.caller = caller
        # Internal field. Ignore this.
        self.data_set_name = data_set_name
        # Total number of words in the conversation.
        self.duration = duration
        # Call duration.
        self.duration_audio = duration_audio
        # File ID, which is the callId in the request parameters. If not specified, a random ID will be generated.
        self.id = id
        # Recording file name.
        self.name = name
        # Internal field. Ignore it.
        self.primary_id = primary_id
        # Custom data 1.
        self.remark_1 = remark_1
        # Custom data 2.
        self.remark_2 = remark_2
        # Custom data 3.
        self.remark_3 = remark_3
        # Recording file URL, used for playback.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business is not None:
            result['Business'] = self.business

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_time is not None:
            result['CallTime'] = self.call_time

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.duration_audio is not None:
            result['DurationAudio'] = self.duration_audio

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id

        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1

        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2

        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('DurationAudio') is not None:
            self.duration_audio = m.get('DurationAudio')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')

        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')

        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')

        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetSyncResultResponseBodyDataHitResult(DaraModel):
    def __init__(
        self,
        hits: List[main_models.GetSyncResultResponseBodyDataHitResultHits] = None,
        name: str = None,
        review_result: int = None,
        rid: str = None,
        type: str = None,
    ):
        # Specific hit location information. At the sentence dimension, returns which condition in the rule was hit and which specific characters triggered the hit within the sentence.
        self.hits = hits
        # Hit rule name.
        self.name = name
        # Review accuracy; possible values: 0 (fault); 1 (correct).
        self.review_result = review_result
        # Hit rule ID.
        self.rid = rid
        # Rule type associated with the hit rule.
        self.type = type

    def validate(self):
        if self.hits:
            for v1 in self.hits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hits'] = []
        if self.hits is not None:
            for k1 in self.hits:
                result['Hits'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hits = []
        if m.get('Hits') is not None:
            for k1 in m.get('Hits'):
                temp_model = main_models.GetSyncResultResponseBodyDataHitResultHits()
                self.hits.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetSyncResultResponseBodyDataHitResultHits(DaraModel):
    def __init__(
        self,
        cid: List[str] = None,
        key_words: List[main_models.GetSyncResultResponseBodyDataHitResultHitsKeyWords] = None,
        phrase: main_models.GetSyncResultResponseBodyDataHitResultHitsPhrase = None,
    ):
        # List of hit condition IDs.
        self.cid = cid
        # Returns the specific characters in the current sentence that hit the rule, which are the keywords to be highlighted.
        self.key_words = key_words
        # Details of the sentence that hit the current rule.
        self.phrase = phrase

    def validate(self):
        if self.key_words:
            for v1 in self.key_words:
                 if v1:
                    v1.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        result['KeyWords'] = []
        if self.key_words is not None:
            for k1 in self.key_words:
                result['KeyWords'].append(k1.to_map() if k1 else None)

        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        self.key_words = []
        if m.get('KeyWords') is not None:
            for k1 in m.get('KeyWords'):
                temp_model = main_models.GetSyncResultResponseBodyDataHitResultHitsKeyWords()
                self.key_words.append(temp_model.from_map(k1))

        if m.get('Phrase') is not None:
            temp_model = main_models.GetSyncResultResponseBodyDataHitResultHitsPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class GetSyncResultResponseBodyDataHitResultHitsPhrase(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        # The Start Time of this sentence, represented as an offset in milliseconds from the starting point.
        self.begin = begin
        # Emotion intensity value ranging from 1 to 10. A higher value indicates stronger emotion.
        self.emotion_value = emotion_value
        # The End Time of this sentence, represented as an offset in milliseconds from the starting point.
        self.end = end
        # The role in the conversation content. Possible values: agent, Customer, System.
        self.role = role
        # Internal field. Ignore.
        self.silence_duration = silence_duration
        # The speech rate of this sentence.
        self.speech_rate = speech_rate
        # A sentence spoken by this role.
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.role is not None:
            result['Role'] = self.role

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class GetSyncResultResponseBodyDataHitResultHitsKeyWords(DaraModel):
    def __init__(
        self,
        cid: str = None,
        from_: int = None,
        to: int = None,
        val: str = None,
    ):
        # The ID of the condition that was hit.
        self.cid = cid
        # The starting character position (inclusive) of the keyword to be highlighted. The value starts from 0 and can be at most the total number of characters in the sentence minus 1.
        self.from_ = from_
        # The ending character position (exclusive) of the keyword to be highlighted. The maximum value is the total number of characters in the sentence minus 1. For example, in the sentence “不可能给你退货的”, if from=0 and to=3, the highlighted keyword is “不可能”, which consists of three characters.
        self.to = to
        # The exact keyword content.
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        if self.val is not None:
            result['Val'] = self.val

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Val') is not None:
            self.val = m.get('Val')

        return self

class GetSyncResultResponseBodyDataAsrResult(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        # The start time of this sentence, which is the offset from the starting point in milliseconds.
        self.begin = begin
        # Emotion intensity value ranging from 1 to 10. A higher value indicates stronger emotion.
        self.emotion_value = emotion_value
        # The end time of this sentence, which is the offset from the starting point in milliseconds.
        self.end = end
        # Role in the dialogue content. Possible values: agent, Customer.
        self.role = role
        # Internal field. Ignore it.
        self.silence_duration = silence_duration
        # The average speech rate of this sentence, in characters per minute.
        self.speech_rate = speech_rate
        # Dialogue content.
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.role is not None:
            result['Role'] = self.role

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class GetSyncResultResponseBodyDataAgent(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        skill_group: str = None,
    ):
        # Agent ID.
        self.id = id
        # Agent name
        self.name = name
        # Skill group name
        self.skill_group = skill_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')

        return self

