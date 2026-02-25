# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryFpShotJobListResponseBody(DaraModel):
    def __init__(
        self,
        fp_shot_job_list: main_models.QueryFpShotJobListResponseBodyFpShotJobList = None,
        next_page_token: str = None,
        non_exist_ids: main_models.QueryFpShotJobListResponseBodyNonExistIds = None,
        request_id: str = None,
    ):
        self.fp_shot_job_list = fp_shot_job_list
        # The token that is used to retrieve the next page of the query results. The value is a 32-bit UUID. If the returned query results cannot be displayed within one page, this parameter is returned. The value of this parameter is updated for each query.
        self.next_page_token = next_page_token
        self.non_exist_ids = non_exist_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.fp_shot_job_list:
            self.fp_shot_job_list.validate()
        if self.non_exist_ids:
            self.non_exist_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_shot_job_list is not None:
            result['FpShotJobList'] = self.fp_shot_job_list.to_map()

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.non_exist_ids is not None:
            result['NonExistIds'] = self.non_exist_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpShotJobList') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobList()
            self.fp_shot_job_list = temp_model.from_map(m.get('FpShotJobList'))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('NonExistIds') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyNonExistIds()
            self.non_exist_ids = temp_model.from_map(m.get('NonExistIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryFpShotJobListResponseBodyNonExistIds(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

class QueryFpShotJobListResponseBodyFpShotJobList(DaraModel):
    def __init__(
        self,
        fp_shot_job: List[main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJob] = None,
    ):
        self.fp_shot_job = fp_shot_job

    def validate(self):
        if self.fp_shot_job:
            for v1 in self.fp_shot_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShotJob'] = []
        if self.fp_shot_job is not None:
            for k1 in self.fp_shot_job:
                result['FpShotJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot_job = []
        if m.get('FpShotJob') is not None:
            for k1 in m.get('FpShotJob'):
                temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJob()
                self.fp_shot_job.append(temp_model.from_map(k1))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        creation_time: str = None,
        duration: int = None,
        file_id: str = None,
        finish_time: str = None,
        fp_shot_config: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotConfig = None,
        fp_shot_result: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResult = None,
        id: str = None,
        input: str = None,
        input_file: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobInputFile = None,
        message: str = None,
        pipeline_id: str = None,
        state: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.creation_time = creation_time
        self.duration = duration
        self.file_id = file_id
        self.finish_time = finish_time
        self.fp_shot_config = fp_shot_config
        self.fp_shot_result = fp_shot_result
        self.id = id
        self.input = input
        self.input_file = input_file
        self.message = message
        self.pipeline_id = pipeline_id
        self.state = state
        self.user_data = user_data

    def validate(self):
        if self.fp_shot_config:
            self.fp_shot_config.validate()
        if self.fp_shot_result:
            self.fp_shot_result.validate()
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.fp_shot_config is not None:
            result['FpShotConfig'] = self.fp_shot_config.to_map()

        if self.fp_shot_result is not None:
            result['FpShotResult'] = self.fp_shot_result.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.input is not None:
            result['Input'] = self.input

        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.state is not None:
            result['State'] = self.state

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('FpShotConfig') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotConfig()
            self.fp_shot_config = temp_model.from_map(m.get('FpShotConfig'))

        if m.get('FpShotResult') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResult()
            self.fp_shot_result = temp_model.from_map(m.get('FpShotResult'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('InputFile') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobInputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResult(DaraModel):
    def __init__(
        self,
        audio_fp_shots: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShots = None,
        fp_shots: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShots = None,
        text_fp_shots: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShots = None,
    ):
        self.audio_fp_shots = audio_fp_shots
        self.fp_shots = fp_shots
        self.text_fp_shots = text_fp_shots

    def validate(self):
        if self.audio_fp_shots:
            self.audio_fp_shots.validate()
        if self.fp_shots:
            self.fp_shots.validate()
        if self.text_fp_shots:
            self.text_fp_shots.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_fp_shots is not None:
            result['AudioFpShots'] = self.audio_fp_shots.to_map()

        if self.fp_shots is not None:
            result['FpShots'] = self.fp_shots.to_map()

        if self.text_fp_shots is not None:
            result['TextFpShots'] = self.text_fp_shots.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFpShots') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShots()
            self.audio_fp_shots = temp_model.from_map(m.get('AudioFpShots'))

        if m.get('FpShots') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShots()
            self.fp_shots = temp_model.from_map(m.get('FpShots'))

        if m.get('TextFpShots') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShots()
            self.text_fp_shots = temp_model.from_map(m.get('TextFpShots'))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShots(DaraModel):
    def __init__(
        self,
        text_fp_shot: List[main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShot] = None,
    ):
        self.text_fp_shot = text_fp_shot

    def validate(self):
        if self.text_fp_shot:
            for v1 in self.text_fp_shot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TextFpShot'] = []
        if self.text_fp_shot is not None:
            for k1 in self.text_fp_shot:
                result['TextFpShot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.text_fp_shot = []
        if m.get('TextFpShot') is not None:
            for k1 in m.get('TextFpShot'):
                temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShot()
                self.text_fp_shot.append(temp_model.from_map(k1))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShot(DaraModel):
    def __init__(
        self,
        primary_key: str = None,
        similarity: str = None,
        text_fp_shot_slices: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlices = None,
    ):
        self.primary_key = primary_key
        self.similarity = similarity
        self.text_fp_shot_slices = text_fp_shot_slices

    def validate(self):
        if self.text_fp_shot_slices:
            self.text_fp_shot_slices.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        if self.text_fp_shot_slices is not None:
            result['TextFpShotSlices'] = self.text_fp_shot_slices.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        if m.get('TextFpShotSlices') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlices()
            self.text_fp_shot_slices = temp_model.from_map(m.get('TextFpShotSlices'))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlices(DaraModel):
    def __init__(
        self,
        text_fp_shot_slice: List[main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlicesTextFpShotSlice] = None,
    ):
        self.text_fp_shot_slice = text_fp_shot_slice

    def validate(self):
        if self.text_fp_shot_slice:
            for v1 in self.text_fp_shot_slice:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TextFpShotSlice'] = []
        if self.text_fp_shot_slice is not None:
            for k1 in self.text_fp_shot_slice:
                result['TextFpShotSlice'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.text_fp_shot_slice = []
        if m.get('TextFpShotSlice') is not None:
            for k1 in m.get('TextFpShotSlice'):
                temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlicesTextFpShotSlice()
                self.text_fp_shot_slice.append(temp_model.from_map(k1))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlicesTextFpShotSlice(DaraModel):
    def __init__(
        self,
        duplication_text: str = None,
        input_fragment: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlicesTextFpShotSliceInputFragment = None,
        input_text: str = None,
        similarity: str = None,
    ):
        self.duplication_text = duplication_text
        self.input_fragment = input_fragment
        self.input_text = input_text
        self.similarity = similarity

    def validate(self):
        if self.input_fragment:
            self.input_fragment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duplication_text is not None:
            result['DuplicationText'] = self.duplication_text

        if self.input_fragment is not None:
            result['InputFragment'] = self.input_fragment.to_map()

        if self.input_text is not None:
            result['InputText'] = self.input_text

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DuplicationText') is not None:
            self.duplication_text = m.get('DuplicationText')

        if m.get('InputFragment') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlicesTextFpShotSliceInputFragment()
            self.input_fragment = temp_model.from_map(m.get('InputFragment'))

        if m.get('InputText') is not None:
            self.input_text = m.get('InputText')

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultTextFpShotsTextFpShotTextFpShotSlicesTextFpShotSliceInputFragment(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        self.duration = duration
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShots(DaraModel):
    def __init__(
        self,
        fp_shot: List[main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShot] = None,
    ):
        self.fp_shot = fp_shot

    def validate(self):
        if self.fp_shot:
            for v1 in self.fp_shot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShot'] = []
        if self.fp_shot is not None:
            for k1 in self.fp_shot:
                result['FpShot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot = []
        if m.get('FpShot') is not None:
            for k1 in m.get('FpShot'):
                temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShot()
                self.fp_shot.append(temp_model.from_map(k1))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShot(DaraModel):
    def __init__(
        self,
        fp_shot_slices: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlices = None,
        primary_key: str = None,
        similarity: str = None,
    ):
        self.fp_shot_slices = fp_shot_slices
        self.primary_key = primary_key
        self.similarity = similarity

    def validate(self):
        if self.fp_shot_slices:
            self.fp_shot_slices.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_shot_slices is not None:
            result['FpShotSlices'] = self.fp_shot_slices.to_map()

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpShotSlices') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlices()
            self.fp_shot_slices = temp_model.from_map(m.get('FpShotSlices'))

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlices(DaraModel):
    def __init__(
        self,
        fp_shot_slice: List[main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSlice] = None,
    ):
        self.fp_shot_slice = fp_shot_slice

    def validate(self):
        if self.fp_shot_slice:
            for v1 in self.fp_shot_slice:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShotSlice'] = []
        if self.fp_shot_slice is not None:
            for k1 in self.fp_shot_slice:
                result['FpShotSlice'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot_slice = []
        if m.get('FpShotSlice') is not None:
            for k1 in m.get('FpShotSlice'):
                temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSlice()
                self.fp_shot_slice.append(temp_model.from_map(k1))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSlice(DaraModel):
    def __init__(
        self,
        duplication: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSliceDuplication = None,
        input: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSliceInput = None,
        similarity: str = None,
    ):
        self.duplication = duplication
        self.input = input
        self.similarity = similarity

    def validate(self):
        if self.duplication:
            self.duplication.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duplication is not None:
            result['Duplication'] = self.duplication.to_map()

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duplication') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSliceDuplication()
            self.duplication = temp_model.from_map(m.get('Duplication'))

        if m.get('Input') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSliceInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSliceInput(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        self.duration = duration
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultFpShotsFpShotFpShotSlicesFpShotSliceDuplication(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        self.duration = duration
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShots(DaraModel):
    def __init__(
        self,
        fp_shot: List[main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShot] = None,
    ):
        self.fp_shot = fp_shot

    def validate(self):
        if self.fp_shot:
            for v1 in self.fp_shot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShot'] = []
        if self.fp_shot is not None:
            for k1 in self.fp_shot:
                result['FpShot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot = []
        if m.get('FpShot') is not None:
            for k1 in m.get('FpShot'):
                temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShot()
                self.fp_shot.append(temp_model.from_map(k1))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShot(DaraModel):
    def __init__(
        self,
        fp_shot_slices: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlices = None,
        primary_key: str = None,
        similarity: str = None,
    ):
        self.fp_shot_slices = fp_shot_slices
        self.primary_key = primary_key
        self.similarity = similarity

    def validate(self):
        if self.fp_shot_slices:
            self.fp_shot_slices.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_shot_slices is not None:
            result['FpShotSlices'] = self.fp_shot_slices.to_map()

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpShotSlices') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlices()
            self.fp_shot_slices = temp_model.from_map(m.get('FpShotSlices'))

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlices(DaraModel):
    def __init__(
        self,
        fp_shot_slice: List[main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSlice] = None,
    ):
        self.fp_shot_slice = fp_shot_slice

    def validate(self):
        if self.fp_shot_slice:
            for v1 in self.fp_shot_slice:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FpShotSlice'] = []
        if self.fp_shot_slice is not None:
            for k1 in self.fp_shot_slice:
                result['FpShotSlice'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fp_shot_slice = []
        if m.get('FpShotSlice') is not None:
            for k1 in m.get('FpShotSlice'):
                temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSlice()
                self.fp_shot_slice.append(temp_model.from_map(k1))

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSlice(DaraModel):
    def __init__(
        self,
        duplication: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSliceDuplication = None,
        input: main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSliceInput = None,
        similarity: str = None,
    ):
        self.duplication = duplication
        self.input = input
        self.similarity = similarity

    def validate(self):
        if self.duplication:
            self.duplication.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duplication is not None:
            result['Duplication'] = self.duplication.to_map()

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duplication') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSliceDuplication()
            self.duplication = temp_model.from_map(m.get('Duplication'))

        if m.get('Input') is not None:
            temp_model = main_models.QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSliceInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSliceInput(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        self.duration = duration
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotResultAudioFpShotsFpShotFpShotSlicesFpShotSliceDuplication(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        self.duration = duration
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class QueryFpShotJobListResponseBodyFpShotJobListFpShotJobFpShotConfig(DaraModel):
    def __init__(
        self,
        fp_dbid: str = None,
        primary_key: str = None,
        save_type: str = None,
    ):
        self.fp_dbid = fp_dbid
        self.primary_key = primary_key
        self.save_type = save_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.save_type is not None:
            result['SaveType'] = self.save_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('SaveType') is not None:
            self.save_type = m.get('SaveType')

        return self

